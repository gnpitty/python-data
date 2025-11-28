from apscheduler.schedulers.background import BackgroundScheduler
import time
def job():
    print("Running weekly ETL...")

scheduler = BackgroundScheduler()
# scheduler.add_job(job, 'cron', day_of_week='tue', hour=3)
#scheduler.add_job(job,trigger='cron', day_of_week='mon', hour=11,minute=50)
scheduler.add_job(job, 'interval', minutes=1, id='my_job_id')
scheduler.start()
print("Sleeping.....")

for i in range(20):
    print(f"{i} -Sleeping.....")
    time.sleep(10)
print("Closing scheduler...")