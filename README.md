# CPSC113 Social Todo App 2

The app is made in Django and uses a PostgreSQL database.

This application is hosted on heroku at [this link - CPSC113](http://social-todo-app-2.herokuapp.com/) - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/paragbhtngr/todoapp2
$ pip install -r requirements.txt

$ python manage.py migrate

$ python manage.py runserver

```

Your app should now be running on [localhost:8000](http://localhost:8000/).
