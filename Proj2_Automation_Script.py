#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import os
import webbrowser

os.system('sudo apt update')
os.system('sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl')
os.system('sudo -u postgres psql')
os.system('CREATE DATABASE sreproject;')
os.system("CREATE USER sreprojectuser WITH PASSWORD 'trump';")
os.system("ALTER ROLE sreprojectuser SET client_encoding TO 'utf8';")
os.system("ALTER ROLE sreprojectuser SET default_transaction_isolation TO 'read committed';")
os.system("ALTER ROLE sreprojectuser SET timezone TO 'UTC';")
os.system('GRANT ALL PRIVILEGES ON DATABASE sreproject TO sreprojectuser;')
os.system('\\q')
os.system('sudo -H pip3 install --upgrade pip')
os.system('sudo -H pip3 install virtualenv')
os.system('mkdir ~/sreprojectdir')
os.system('cd ~/sreprojectdir')
os.system('virtualenv sreprojectenv')
os.system('. sreprojectenv/bin/activate')
os.system('pip install django gunicorn psycopg2-binary')
os.system('django-admin.py startproject sreproject ~/sreprojectdir')
os.system('cd ~/sreprojectdir/sreproject')
os.system('cp ~/Automation/settings.py ./settings.py')
os.system('~/sreprojectdir/manage.py makemigrations')
os.system('~/sreprojectdir/manage.py migrate')
os.system('~/sreprojectdir/manage.py createsuperuser')
os.system('apple')
os.system('aasquier@pdx.edu')
os.system('orange')
os.system('orange')
os.system('~/sreprojectdir/manage.py collectstatic')
os.system('yes')

webbrowser.open('https://console.cloud.google.com/compute/instancesDetail/zones/us-central1-a/instances/instance-1?project=cs410-site-reliability-eng&organizationId=39525358122&supportedpurview=project')
input("Press Enter to continue...")

os.system('~/sreprojectdir/manage.py runserver 0.0.0.0:8000')

webbrowser.open('http://34.67.211.3:8000')
input("Press Enter to continue...")

os.system('cd ~/sreprojectdir')
os.system('gunicorn --bind 0.0.0.0:8000 sreproject.wsgi')

webbrowser.open('http://34.67.211.3:8000')
input("Press Enter to continue...")

os.system('sudo su -')
os.system('cd /etc/nginx/sites-available')
os.system('cp /home/aasquier/Automation/sreproject ./')
os.system('chown root ./sreproject')
os.system('ln -s /etc/nginx/sites-available/sreproject ../sites-enabled/sreproject')
os.system('rm ../sites-enabled/default')
os.system('nginx -t')
input("Press Enter to continue...")

os.system('systemctl restart nginx')
webbrowser.open('http://34.67.211.3')
input("Press Enter to continue...")

