from .models import *
from . import twitter_api
from datetime import datetime
from backend.main.analyze import get_analysis_result
from backend.main import twitter_api

def run_update():

    batch_job = {} # {hashtag: [users subscribed to this hashtag]}

    print("SCANNING...")

    # go through all subscriptions and add jobs that need new updates
    subscriptions = Subscription.objects.all()
    for sub in subscriptions:
        # check if ready to scan
        #if not sub.last_scanned or ((datetime.today() - sub.last_scanned).days >= sub.frequency):
        if sub.hashtag_id.topic not in batch_job:
            batch_job[sub.hashtag_id.topic] = []     
        batch_job[sub.hashtag_id.topic].append(sub.user_id.username)

    print("RUNNING ANALYSIS")

    
    if not batch_job:
        print("JOB DONE")
        return 

    # make connection
    conn = twitter_api.create_conn()

    # run analysis on hashtags in batch_job
    for topic, users in batch_job.items():
        get_analysis_result(topic, conn)
        for user in users:
            sub = Subscription.objects.filter(user_id = user).filter(hashtag_id=topic)
            sub.update(last_scanned=datetime.today())

    print("JOB DONE")