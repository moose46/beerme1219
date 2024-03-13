
# To Init Database

    delete all numbered migration files in the migrations directory
    delete all existing tables in the database schema
    py manage.py makemigrations
    py manage.py migrate
    py manage.py createsuperuser

# To load NASCAR drivers

    cd to nascar/scripts
    py ../../manage.py runscript load_drivers_from_csvhttps://books.agiliq.com/projects/django-orm-cookbook/en/latest/subquery.html

# To run server on port 8081

    open bash terminal
    cd beer
    python manage.py runserver 8081

## To view the data in a browser: [Admin](http://127.0.0.1:8081/admin)
