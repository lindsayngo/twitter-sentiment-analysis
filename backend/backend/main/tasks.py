from backend.main.update import run_update
from datetime import timedelta, datetime
import time

def subscription_job():
    while True:
        run_update()
        time.sleep(60 * 30) # runs every 30 mins

subscription_job()
