
# Readme

## Steps

1. git clone
   git clone https://github.com/btrif/colibri_django_rest_framework.git
   
2. Setup virtual env
   Create new environment
   Go to project folder and create the virtual env :

```
python -m venv .colibri_venv
```
3. Activate virtual environment

```.colibri_venv\Scripts\activate.bat           (Windows)
./.colibri_venv/bin/activate                 (Linux, Mac)
```

4. Install requirements.txt
Install the Python libraries inside virtual environment :
```
(.colibri_venv) D:\workspace\colibri_django_rest_framework> pip install -r requirements.txt```
```

5. Start Django server

```
(.colibri_venv) D:\workspace\colibri_django_rest_framework> python manage.py runserver

```