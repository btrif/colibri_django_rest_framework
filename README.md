
# Readme

## Steps

1. Clone github code
```
   git clone https://github.com/btrif/colibri_django_rest_framework.git
```
2. Setup virtual env
   Create new environment
   Go to project folder and create the virtual env :

```
python -m venv .colibri_venv
```
3. Activate virtual environment

```
.colibri_venv\Scripts\activate.bat           (Windows)
./.colibri_venv/bin/activate                 (Linux, Mac)
```

4. Install requirements.txt
Install the Python libraries inside virtual environment :
```
(.colibri_venv) D:\workspace\colibri_django_rest_framework> pip install -r requirements.txt
```

5. Start Django server

```
(.colibri_venv) D:\workspace\colibri_django_rest_framework> python manage.py runserver

```

# Docker alternative
#### Advantage : You can completely ignore the manual setup from above. This will be done automatically for you by Docker.
If you have installed Docker locally on you machine you can do the following
in the root folder of the application :

```bash
D:\workspace\colibri_django_rest_framework>docker build . -t colibri_django_rest_framework:latest
D:\workspace\colibri_django_rest_framework>docker run -p 8000:8000 colibri_django_rest_framework
```

Now  you can already use in the same way the host machine Web Browser Application API.
You should get something like this :
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 07, 2022 - 15:48:35
Django version 4.0.5, using settings 'colibri_django_rest_framework.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```