```bash
pip install django
pip install django-extensions
pip install django-crispy-forms
'''
# To Init Database

    delete all numbered migration files in the migrations directory
    delete all existing tables in the database schema
    py manage.py makemigrations
    py manage.py migrate
    py manage.py createsuperuser

# To load NASCAR drivers

```bash
    cd to nascar/scripts
    python ../../manage.py runscript load_drivers_from_csvhttps://books.agiliq.com/projects/django-orm-cookbook/en/latest/subquery.html
```

# To run server on port 8081

    open bash terminal
    cd beer
    python manage.py runserver 8081

## To view the data in a browser: [Admin](http://127.0.0.1:8081/admin)

## To see which env is activated

```bash
    which python
```

## Django forms

<https://www.geeksforgeeks.org/django-forms/>

## Python: Default Interperter Path

.venv\Scripts\python
