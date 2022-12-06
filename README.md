# Django ORM Storage watch

This tool allows to create a web interface to monitor and navigate the database of storage visits. 

### How to install

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

Before using the tool, you must create a new file called **db_settings.env** in the project folder and fill it with required database settings:
1. `ENGINE`
2. `HOST`
3. `PORT`
4. `NAME`
5. `USER`
6. `PASSWORD`
7. `SECRET_KEY`
8. `DEBUG` - True or False

After creating database settings environment file, you will be able to launch the manage.py file. 
```
python manage.py runserver 0.0.0.0:8000
```
After that, you should open the web interface on your preferred web browser. It should be launched on the IP adress of your local machine with the port `:0000`. For example: 
```
http://127.0.0.1:8000/
```
### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).