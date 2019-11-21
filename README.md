# twitter-sentiment-analysis

## Note
- Your project root is the twitter-sentiment-analysis dir

## Create and Run VirtualEnv
- Prereqs: learn pip and virtualenv
```
sudo pip3 install virtualenv
pip3 install -r requirements.txt
source <wherever your env is>
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