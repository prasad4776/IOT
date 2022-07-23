# **Welcome to the README Section of IOT Project**

## _To Start Using the IOT Project,Below are the pre-requisites:_

> Pre-requisite : Install python3 from https://www.python.org/downloads/

### _1.Creating a virtual environment and activating it._
```
1. pip install virtualenv
2. python3 -m venv env
3. source env/bin/activate
 ```


### _2.Clone the project with the command given below_
```commandline


1. git clone "" 
2. cd iot_project
3. pip install -r requirements.txt 
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py fake_data
7. python manage.py runserver

```
### _3.API Documentation link given below:_

http://localhost:8000/swagger/

### _4. APIs to Test_
```commandline
Credentials to test the login API :- 
email : test@iot.com
password : SorI0t123
```

```commandline

1. login : http://127.0.0.1:8000/login/
2. list of students : http://127.0.0.1:8000/students/all_students
3. create new student : http://127.0.0.1:8000/students/all_students
4. get refresh token : http://127.0.0.1:8000/get_refresh_token/

```

>For all the above APIs, use API documentation link
to know the required fields, request method and
required header.


>API number 2,3 need bearer token to be passed.

> JWT Access token's life is 2 minutes,after that it expires.
To obtain new token use API number 4
and pass refresh token in the body.

