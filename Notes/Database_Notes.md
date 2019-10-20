### Steps after changing models:
(1) Applied changes in models.py
(2) run `python manage.py makemigrations` to create migrations for those changes
(3) run `python manage.py migrate` to apply those changes to the database


### Alter database
* Enter python interactive mode using `python manage.py shell`
* Create new model object: `q = Question(question_text="What's new?", pub_date=timezone.now())`
* Save it: `q.save()`
* Access data members: `q.question_text`
* Update members: `q.question_text = "What's up?"`
* Display all questions in the database: `Question.objects.all()`

After initial setup you can alter data through `/admin`: http://127.0.0.1:8000/admin/

