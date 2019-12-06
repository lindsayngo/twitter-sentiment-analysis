from djongo import models

class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)

class Hashtag(models.Model):
    topic = models.CharField(max_length=255, primary_key=True)
    last_scanned = models.DateTimeField()

class Subscription(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hashtag_id = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    frequency = models.IntegerField() # in days
    checked_since = models.IntegerField() #tracks when a subscription is ready to be checked

class Job(models.Model):
    # fields needed for cron job, fill in when figured out
    
    class Meta: 
        abstract = True

class Queue(models.Model):
    job = models.EmbeddedModelField(model_container = Job)

class DataPoint(models.Model):
    time = models.DateTimeField() # sentiment analysis run date
    # value cannot be decimal due to sqlparse djongo compatibility bug
    value = models.IntegerField() # sentiment result percentage 

    class Meta:
        abstract = True

class Analysis(models.Model):
    hashtag_id = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    timeseries = models.ArrayModelField(model_container = DataPoint)
