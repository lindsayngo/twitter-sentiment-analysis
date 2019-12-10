# twitter-sentiment-analysis

## Note
- Your <proj-root> is the twitter-sentiment-analysis dir

## Create and Run VirtualEnv
- Prereqs: learn pip and virtualenv
```
sudo pip3 install virtualenv
pip3 install -r requirements.txt
source <path-to-env>/bin/activate
```

## Configuring Database
- Prereqs: get mongo running locally 
  
Run the mongo daemon ```mongod```

If you don't know where to store your data, run it in your project root
```
mongod --noauth --dbpath mongo/data
```

## Run Django 
- Prereqs: learn you some django
```
python3 manage.py runserver
```

## Run scheduler
```
python3 manage.py process_tasks
```

## Build Angular
- This would build the angular projects and bring them to django
```
ng build --prod --output-path <proj-root>\backend\backend\main\static --watch --output-hashing none
```

## Build & Run Docker Compose
- prereq: learn you some docker & install docker-compose
```
docker-compose build
docker-compose up
```