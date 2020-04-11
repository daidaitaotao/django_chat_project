# A Django chatbot project
The project lays the groundwork for storing, customizing, and managing questions that can be used by a chatbot
within a conversation with a user.  Questions may be customized based on specific user attributes, and both
CLI and web interfaces exist for managing them.  All work has been done in Python using Django, and can be easily 
bootstrapped using the installation instructions below.

## Structure
In order support the use of user-targeted questions in communications between a chatbot and a user, the domain/db 
will follow the following structure:
- Account
    - User: track user login information
    
    - UserProfile: track user metadata such as age and gender, which can help customize question
- Chat (MyApp)
    - BaseQuestion: the original question which all customized questions can track back to. Each base question has topic associate to it to categorize the question.
    - Question: the customized question based off configuration such as user's age and gender. Each question has base question to trace back to.
    - Response: user response to a Question object.

    - QuestionChangeHistory: a record of the change history of a base question or question, while allows for the tracking how question get customized over time.

## Installation
The code base can be run this locally or on Docker.

#### Requirements to Run
- Local Requirements
  - Python 3.7 +
    - library: virtualenv
- Docker Requirements
  - Docker Compose
  - Docker

#### Pulling Down Project
```
mkdir your_dir
cd your_dir
git clone #repo
cd django_chat_project
source app/env/bin/activate
```

#### Run on docker
This is not required if running locally.
```
# update permission locally
chmod +x app/entrypoint.sh

# build docker image and run
docker-compose up -d --build

# load fixture data (optional), it will create the superuser too
docker-compose exec web python manage.py loaddata fixture_data.json

# if you did not choose to load the fixture data, create superuser
docker-compose exec web python manage.py createsuperuser
```

#### Run locally
This is not required if running in Docker.
```
cd app
pip install -r requirements_local.txt

# create db
psql
CREATE USER local_user WITH PASSWORD 'password123';
CREATE DATABASE django_chat WITH OWNER local_user;

# load fixtures data (optional)
python manage.py loaddata fixture_data.json

# if did not run loaddata, then create superuser mannually
python manage.py createsuperuser

# finally
python manage.py runserver
```

#### Verify System Started Correctly
Go to http://localhost:8000/admin and enter the following credentials:

`username: admin ` `password: password123` 

After logging in successfully, should should be able to see a page similar to:

![screenshot](screenshot_admin.png)

## Access through API
There are three endpoints for access chatbot data, **PLEASE** make sure you have logged in as superuser since only 
 administrators are allowed to view and update question data directly.

- /myapp/base-question/
    * allowed method: [GET, POST]

- /myapp/question/
    * allowed method: [GET, POST]
    * query_param:
        * base_question: base_question_id

- /myapp/question-change-history/
    * allowed method: [GET]
    * query_param:
        * base_question: base_question_id
        * question: question_id

##### Examples:
http://localhost:8000/myapp/question-change-history/?question=2

![screenshot](screenshot_drf_api.png)

http://localhost:8000/myapp/question/
![screenshot](screenshot_create_question.png)


## Access through command
There are two commands in this repo
- add_base_question - create a base question
- get_question_change_history - get change history of one question
##### examples:
```
python manage.py add_base_question body="this is a new question" topic="information" -rt 1
(docker) docker-compose exec web python manage.py add_base_question body="this is another new question" topic="information"
(docker) docker-compose exec web python manage.py get_question_change_history -q_id=1
```
example response:
```
(env) user@computer app % docker-compose exec web python manage.py get_question_change_history -q_id=1
[OrderedDict([('base_question', 1), ('question', 1), ('date_created', '2020-04-11T15:10:56.755000Z'), ('before_body', 'How do you feel today? sir'), ('after_body', 'How are you today? sir'), ('diff', {'add': [{'value': 'a', 'index_pos': 6}, {'value': 'r', 'index_pos': 7}, {'value': 'e', 'index_pos': 8}], 'delete': [{'value': 'd', 'index_pos': 4}, {'value': 'o', 'index_pos': 5}, {'value': ' ', 'index_pos': 13}, {'value': 'f', 'index_pos': 14}, {'value': 'e', 'index_pos': 15}, {'value': 'e', 'index_pos': 16}, {'value': 'l', 'index_pos': 17}]})])]
```

## Additional Notes:
This project is using **signal**(https://docs.djangoproject.com/en/3.0/ref/signals/) to track the BaseQuestion/Question object change history.
Whenever a BaseQuestion or a Question changes, it will create a record in the QuestionChangeHistory table.

## What went well
1. The requirements of this project are straight forward.
2. Most functionality in the requirements can be implemented by Django and Django Rest Framework.

## What was difficult
1. To understand the logic of how questions evolve over time in order to come up with a Domain and Database design.
2. The initial system setup took more time than expected.

## What could do better
1. Write Unit test
2. Write test for the endpoints
3. Potential feature enhancements:
    * make QuestionChangeHistory `diff` attribute easier to read.
    * currently on the Question table, the age and gender related fields are stored as columns. It could be 
    better to have those configuration stored in one JSON field, so we have the flexibility to add additional
    configuration.
    * currently `Topic` are stored as enum in BaseQuestion table, we could consider make Topic as its own table.
    * there is no work has been done for the logic to implement a conversation because this is outside the scope of 
    original requirements.