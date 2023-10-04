# Step By Step For Create Django CMS Project
## Install the django CMS package
Step 1: Create virtual environments
```
python -m venv venv
```
Step 2: Activate it
```
cd venv\Scripts
```
```
activate
```
Step 3: Install pip
```
python.exe -m pip install --upgrade pip
```
Step 4: Install django v3.2 that stable for cms 
```
pip install django==3.2
```
Step 5: Install django-cms
```
pip install django-cms
```
## Create a new project
Step 1: Create a new project
```
django-admin startproject myproject
```
that result
```
myproject
    myproject
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    manage.py
```