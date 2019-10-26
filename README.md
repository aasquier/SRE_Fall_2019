### Production URIs
Make sure the SQL Server is up and running: ./cloud_sql_proxy \
-instances"cs410-site-reliability-eng:us-west1:polls-instance"=tcp:3306 <br>
Site URI: https://cs410-site-reliability-eng.appspot.com/polls/
Admin URI: https://cs410-site-reliability-eng.appspot.com/admin/

### Local URI
Using the Django Development Server: `~/sreprojectdir/manage.py runserver 0.0.0.0:8000` <br>
Using Gunicorn Application Server (run in `~/sreprojectdir`): `gunicorn --bind 0.0.0.0:8000 sreproject.wsgi` <br>

Website URI Before NGINX: http://34.67.211.3:8000/ <br>
Website URI W/ NGINX: http://34.67.211.3/ <br>
Admin Page: http://34.67.211.3:8000/admin/login/?next=/admin/ (use credentials below) <br>

NGINX Config File location: `/etc/nginx/sites-available/sreproject` <br>

### Install Postgres Database locally mac
Make sure you are in the virtual environment and it's activated: `source sreprojectenv/bin/activate`  
1. `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
2. `brew install postgresql`
3. `brew install nginx`

### Super Secret Credentials
**Admin Login:**<br>
User: admin<br>
Password: MegaPassword<br>

### Deployment Steps
Cloud SQL Instance Connection name: `cs410-site-reliability-eng:us-west1:polls-instance`
1. Make sure you're in the virtual env: `. sreprojectenv/bin/activate`
2. Make any prior database migrations
3. `python manage.py collectstatic`
4. `gcloud app deploy`

### Useful GCloud things
* Display the deployment logs: `gcloud app logs read`
* Open app in browser: `gcloud app browse`

### Migrate Database
1. After making database changes:
2. run `python manage.py makemigrations` to create migrations for those changes
3. run `python manage.py migrate` to apply those changes to the database

### Alter database examples
* Enter python interactive mode using `python manage.py shell`
* Create new model object: `q = Question(question_text="What's new?", pub_date=timezone.now())`
* Save it: `q.save()`
* Access data members: `q.question_text`
* Update members: `q.question_text = "What's up?"`
* Display all questions in the database: `Question.objects.all()`  

After local setup you can alter data through `/admin` e.g. http://127.0.0.1:8000/admin/
