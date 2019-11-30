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
    files['week'] = [int(date.isocalendar()[1])-39 for date in files['dates']]
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

    for date, file in zip(files['dates'], files['names']):
        print('opening file', file)
        codes[date] = {}
        if pathlib.Path(file).suffix == '.gz':
            with gzip.open(file, 'rb') as f:
                codes[date] = extract_codes(f)

        else:
            with open(file, 'r') as f:
                codes[date] = extract_codes(f)

    return codes

                
def main():
    log_file_dir = '/var/log/nginx'
    files = get_log_names(log_file_dir)

    codes = codes_per_date(files)    

    print(codes)
    print(files)


if __name__ == '__main__':
    sys.exit(main())
