from backend.main.update import run_update
from datetime import timedelta, datetime
import time

def subscription_job():
    while True:
        run_update()
        time.sleep(5) # runs every 15s for demo purposes

subscription_job()