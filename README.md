# twitter-sentiment-analysis

## Getting Started
- Git clone the project
- Your ```<proj-root>``` is the twitter-sentiment-analysis dir

## Create and Run VirtualEnv
- Prereqs: learn you some pip and virtualenv
```
sudo pip3 install virtualenv
python3 -m virtualenv env
source <path-to-env>/bin/activate
pip3 install -r requirements.txt
```

## Configuring Database
- Prereqs: get mongo running locally 
  
Run the mongo daemon ```mongod```

If you don't know where to store your data, run it in ```<proj-root>```
```
mkdir mongo/data
mongod --noauth --dbpath mongo/data
```

## Setting up Twitter API Key
- get your own key via [twitter](https://python-twitter.readthedocs.io/en/latest/getting_started.html)
- create a ```<proj-root>/backend/backend/secretkey.py``` file and put key values in here
- settings.py should import the following values:
  - TWT_API_KEY_VAL
  - TWT_API_SECRET_VALUE
  - TWT_ACCESS_TOKEN_VAL
  - TWT_ACCESS_SECRET_VAL

## Run Django 
- Prereqs: learn you some django
```
python3 manage.py runserver
```

## Run Background Task Scheduler
```
python3 manage.py process_tasks
```

## Build & Run Docker Compose
- prereq: learn you some docker & docker-compose
```
docker-compose build
docker-compose up
```