import schedule
import time
from backend.main import update
from update import run_update

def job():
    run_update()
    return schedule.CancelJob

schedule.every(1).minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)