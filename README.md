# This is CMS App with Django and Mysql
To excecute the app you must following steps

1. create virtual environment:

```
python -m virtualenv venv
```

2.   Activate the virtual environment:
```
"venv/Scripts/activate.bat"
```
3.  Install project dependencies:
```
pip install -r requeriments.txt
```
4. Run the migrations:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
5. Run the Django development server:
```
python manage.py runserver
```
