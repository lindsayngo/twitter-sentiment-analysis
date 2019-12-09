from .models import *
from . import twitter_api
from datetime import datetime
from backend.main.analyze import get_analysis_result

def run_update():

    batch_job = {} # {hashtag: [users subscribed to this hashtag]}

    print("SCANNING...")

    # go through all subscriptions and add jobs that need new updates
    subscriptions = Subscription.objects.all()
    for sub in subscriptions:
        # check if ready to scan
        print((datetime.now() - sub.last_scanned).days)
        if (datetime.today() - sub.last_scanned).days >= sub.frequency:
            if sub.hashtag_id.topic not in batch_job:
                batch_job[sub.hashtag_id.topic] = []     
            batch_job[sub.hashtag_id.topic].append(sub.user_id.username)

    print("RUNNING ANALYSIS")

    # run analysis on hashtags in batch_job
    for topic, users in batch_job.items():
        get_analysis_result(topic)
        for user in users:
            sub = Subscription.objects.filter(user_id = user).filter(hashtag_id=topic)
            sub.update(last_scanned=datetime.today())
            print(sub)

    print("JOB DONE")