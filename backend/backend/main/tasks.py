from background_task import background
from backend.main.update import run_update
from datetime import timedelta, datetime
import time

@background(schedule=datetime.now())
def subscription_job():
    run_update()
    time.sleep(15) # runs every 15s for demo purposes