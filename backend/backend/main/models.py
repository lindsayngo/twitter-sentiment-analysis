from djongo import models

class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)

class Hashtag(models.Model):
    topic = models.CharField(max_length=255, primary_key=True)

class Subscription(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hashtag_id = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    frequency = models.IntegerField() # in days
    last_scanned = models.DateTimeField(default=None) # in days

class DataPoint(models.Model):
    time = models.DateTimeField() # sentiment analysis run date
    # value cannot be decimal due to sqlparse djongo compatibility bug
    value = models.IntegerField() # sentiment result percentage 

    class Meta:
        abstract = True

class Analysis(models.Model):
    hashtag_id = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    timeseries = models.ArrayModelField(model_container = DataPoint, default=None, null=True)
