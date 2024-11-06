from celery import Celery, shared_task
from send_email import send_email_function  
import redis
import json
from redis_config import RedisConfig


app = Celery('worker_script', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

client = RedisConfig.create_redis_client()

new_email_list = list()

email_list_data = client.get("email_queue")
if email_list_data:
    new_email_list = json.loads(email_list_data)
    print("Retrieved email list:", new_email_list)
else:
    print("No email list found in Redis.")

@shared_task
def process_emails(email_list):
    for email in email_list:
        print(email)
        send_email_function(email)
    print("All emails sent successfully.")

process_emails(new_email_list)