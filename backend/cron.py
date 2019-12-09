import schedule
import time
from backend.main.update import run_update

def subscription_job():
    run_update()

