### Install Postgres Database locally mac
Make sure you are in the virtual environment and it's activated: `source sreprojectenv/bin/activate`  
(1) `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
(2) brew install postgresql
(3) brew install nginx

### Super Secret Credentials:
Admin Login:
User: admin
Pass: MegaPassword

### Steps after changing models:
(1) Applied changes in models.py
(2) run `python manage.py makemigrations` to create migrations for those changes
(3) run `python manage.py migrate` to apply those changes to the database

### Alter database examples
* Enter python interactive mode using `python manage.py shell`
* Create new model object: `q = Question(question_text="What's new?", pub_date=timezone.now())`
* Save it: `q.save()`
* Access data members: `q.question_text`
* Update members: `q.question_text = "What's up?"`
* Display all questions in the database: `Question.objects.all()`  

After local setup you can alter data through `/admin` e.g. http://127.0.0.1:8000/admin/
