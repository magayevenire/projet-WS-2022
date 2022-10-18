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
    `env\Scripts\activate.bat` (Windows)
    `source env\bin\activate` (Linux)

5. `pip install -r requirements.txt`

### mise à jour de la basse de donnèe 
    python manage.py makemigrations 
    python manage.py migrate `

### admin 
    python manage.py createsuperuser

- username : admin
- password : passer123

### lancer le serveur 
    python manage.py runserver

### sample usage 
- create user
    curl -X POST http://127.0.0.1:8000/api/auth/users/ --data 'username=magaye&password=passer123'

`{"email": "", "username": "djoser", "id":1}`

- login 
    curl -X POST http://127.0.0.1:8088/auth/token/login/ --data 'username=djoser&password=alpine12'
`{"auth_token": "b704c9fc3655635646356ac2950269f352ea1139"}`

- user
    curl -LX GET http://127.0.0.1:8088/auth/users/me/ -H 'Authorization: Token b704c9fc3655635646356ac2950269f352ea1139'
`{"email": "", "username": "djoser", "id": 1}`

- [djoser](https://djoser.readthedocs.io/en/latest/sample_usage.html)
