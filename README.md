# projet-WS-2022" 

# Server

## Configuration de l'environnement de travail 

### Prérequis
1. Installer python [ici](https://www.python.org/downloads/)


### Installations des dépendances

    (*) => sous windows remplacer python par py  
1. Naviguer dans le repertoire

2. `python -m pip install virtualenv` (*) 

3. `python -m venv env` (*)

4. Activer l'environnement virtuel
    - `env\Scripts\activate.bat` (Windows)
    - `source env\bin\activate` (Linux)

5. `pip install -r requirements.txt`

### initialiser la base de donnée (seulment la première fois
    - `python manage.py makemigrations `
    - `python manage.py migrate `
### lancer le serveur 
-   `python manage.py runserver`

# admin 
link : http://127.0.0.1:8000/admin 

- username : admin
- password : passer123





