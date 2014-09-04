# TDDbin.com backend

TDDbin - for getting hooked to TDD in no time


# First time setup

1) In order to setup python, django, mysql, etc. run `./setup-local-dev-python-env.sh`.
   This will create a directory `python-env` containing all necessary packages.
2) In there `. ./python-env/bin/activate` will start the environment where
   you should then start the django server in, see below.

- make sure to have started mysql (e.g. using `mysqld_safe`) and created a database (e.g. named 'tddbin')
- create the initial DB content `python src/manage.py syncdb; python src/manage.py migrate`

In case the setup in step 1) fails, try this:
- install mysql-python, i.e. using `pip install MySQL-python` (may need to use `sudo`)
- make sure mysql_config is in the path


# Local development

To run the web site (using the django dev server), do the following

- make sure to have started mysql (e.g. using `mysqld_safe`)
- from this directory run `. ./python-env/bin/activate` to switch into the virtualenv provided for this project
- to start the webserver do `python src/manage.py runserver_plus` or less verbose `python src/manage.py runserver`


To sync your database
- `python src/manage.py migrate`

DB schema migrations, since django 1.7 included (no need for South anymore)

When you have changed a model and want to synchronize the DB, run:
1) `cd <your-projects-dir>/tddbin-backend` make sure you are in the right dir
2) `python src/manage.py makemigrations` generate the migration code for the model change you just made
3) `python src/manage.py migrate` migrate the DB, which plays all changes on top of the current DB


# DB setup

- `pip install mysql-python`
- in your mysql console `CREATE DATABASE tddbin DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;`

# Tests

How to run the django tests?
- `cd tddbin.com/src` and `clear; python manage.py test tddbin --noinput`



# ???????????????????? old stuff below (copied from tddbin.com)
????????????????????????????????? fixes needed from here, when the structure has all this stuff ...
GitHub auth setup
-----------------
- go to https://github.com/organizations/uxebu/settings/applications
- for "tddbin.com-local testing" copy
  * Client ID
  * Client Secret
- in the django admin, make sure to have the site with the value of `settings.SITE_ID` (most probably 1)
- in the django admin, open http://127.0.0.1:8000/admin/socialaccount/socialapp/add/
  * as provider use GitHub
  * Name: whatever you like
  * use client ID and client secret as you copied before
  * !!! make sure the site with the `settings.SITE_ID` is added to the right box
  * SAVE
- social auth should work now

Forgot your password?
---------------------

    Open the django shell: `python src/manage.py shell`
    and in there do the following

    >>> from tddbin_com.models import User
    >>> me = User.objects.get(username='wolframkriesing')
    >>> me.set_password('1')
    >>> me.save()


Start a local email server
--------------------------

    python -m smtpd -n -c DebuggingServer localhost:1025


FAQ
---

- When running the tests I get "address already in use". What can I do?
  Maybe chromedriver that is used by selenium has not terminated
  correctly. Call `killall chromedriver` on the command line and you should be fine.
