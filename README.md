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
- get your own key
- create a ```<proj-root>/backend/backend/secretkey.py``` file and put key in here
- settings.py will import the key set as TWT_API_SECRET_VALUE

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