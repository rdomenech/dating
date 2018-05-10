# crawler
Technical test as Python developer in retoglobal

## How to use it
- Open a terminal.
- Download the source code.
- Create a virtualenv or virtualenwrapper with python 3.x.
- Install the requirements.
- Open mysql: 
```bash
$ mysql -u root -p -h 127.0.0.1
```
```mysql
CREATE DATABASE <DATABASE_NAME>;
CREATE USER '<USERNAME>'@'<HOST>' IDENTIFIED BY '<PASSWORD>';
GRANT ALL PRIVILEGES ON <DATABASE_NAME>.* TO 'USERNAME'@'HOST';
GRANT ALL PRIVILEGES ON test_<DATABASE_NAME>.* TO 'USERNAME'@'HOST';
```
- Run it inside the project path:
```bash
$ ./manage.py migrate
$ ./manage.py runserver
```
- Then you can query the API with Postman.
- To run the tests:
```bash
$ ./manage.py tests
```
