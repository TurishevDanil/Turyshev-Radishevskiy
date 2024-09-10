## Initial installation of tools and packages

> Note: Creating and using virtual environments.

Сreating venv python [mac].

```sh
python3 -m venv venv
```

Сreating venv python [windows].

```sh
python -m venv venv

python -m venv .venv
```

Activating venv python [mac].

```sh
source venv/bin/activate 
```
Activating venv python [windows -> powershell].

```sh
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

venv\Scripts\Activate.ps1
```

Deactivation venv python.

```sh
deactivate
```

> Note: Create and use an application dependency file.

Getting a list of packages used in a project

```sh
pip freeze
```

Recording a list of packages used in the project
```sh
python -m pip freeze > requirements.txt
```

Installing packages used in the project from the list
```sh
python -m pip install -r requirements.txt
```
Basic Django Commands
```sh
pip install django==4.2 -> installing django package version
django-admin startproject "name project" ->  creating a new project
python manage.py runserver -> starting django server, Quit the server with CTRL-BREAK
python manage.py migrate -> runs migrations on the database
```