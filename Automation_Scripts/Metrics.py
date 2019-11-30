import os
import sys
import gzip
import pathlib
import datetime
import http.client
from glob import glob



def get_log_names(dir):
  
    files = {} 
    files['names'] = glob(os.path.join(dir, 'access*'))
    files['dates'] = [datetime.datetime.fromtimestamp(os.stat(file).st_mtime) for file in files['names']]
    files['week'] = [str(int(date.isocalendar()[1])-39) for date in files['dates']]
    files['dates'] = [date.strftime("%d-%b-%Y") for date in files['dates']]
    return files


def extract_codes(f):
    codes = {}
    for line in f.readlines():
        code = str(line).split(' ')[8]
        if code.isnumeric():
                if code in codes:
                    codes[code] += 1
                else:
                    codes[code] = 1

    return codes


def codes_per_date(files):

    codes = {}

    for date, file, week in zip(files['dates'], files['names'], files['week']):
        print('opening file', file)
        if pathlib.Path(file).suffix == '.gz':
            with gzip.open(file, 'rb') as f:
                codes[date] = extract_codes(f)

        else:
            with open(file, 'r') as f:
                codes[date] = extract_codes(f)

        codes[date].update({'week':week})

    return codes


def codes_per_week(codes_daily):
    
    codes = {}

    for date in codes_daily:
        week = codes_daily[date]['week']
        if week not in codes:
            codes[week] = codes_daily[date] 
            codes[week].pop('week', None)
        else:
            for key in codes_daily[date]:
                if key in codes[week] and key != 'week':
                    codes[week][key] += codes_daily[date][key]
                elif key != 'week':
                    codes[week][key] = codes_daily[date][key]

    return codes


def main():
    log_file_dir = '/var/log/nginx'
    files = get_log_names(log_file_dir)

    codes_daily = codes_per_date(files)    

    codes_weekly = codes_per_week(codes_daily)

    print(files)
    print(codes_daily)
    print(codes_weekly)


if __name__ == '__main__':
    sys.exit(main())
