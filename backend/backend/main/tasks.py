from background_task import background
from backend.main.update import run_update
from datetime import timedelta, datetime
from background_task.models import Task

@background(schedule=5)
def subscription_job():
    print("hellow")
    # run_update()

subscription_job(repeat=3)