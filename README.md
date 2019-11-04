# CVR Time Table management system

### Install Django
```
pip3 install Django
```

### For Django db admin
```
sudo apt install libmysqlclient-dev
pip3 install mysqlclient

```

### To setup db in django admin
* go to the database folder inside the repo and type the following in the terminal
```
source ./venv/bin/activate
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

### To access database admin interface
go to the database folder inside the repo and type the following in the terminal

```
source ./venv/bin/activate
python3 manage.py runserver
```