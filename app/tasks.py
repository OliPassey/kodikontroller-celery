from celery.schedules import crontab
from .celery_app import celery
from celery.utils.log import get_task_logger
import requests

logger = get_task_logger(__name__)

@celery.task
def call_host_status():
    base_url = celery.conf.get('kk_base_url', 'http://localhost:5000')
    endpoint = "/admin/host_status"
    full_url = f"{base_url}{endpoint}"

    logger.info("Executing call_host_status")
    response = requests.get(full_url)
    logger.info(f"Status code: {response.status_code}, Data: {response.text}")
    return {'status': response.status_code, 'data': response.text}

# Use the configuration to setup periodic task schedule
schedule_minutes = celery.conf.get('HOST_STATUS_SCHEDULE_MINUTES', '*/5')
celery.conf.beat_schedule = {
    'call-host-status-according-to-schedule': {
        'task': 'app.tasks.call_host_status',
        'schedule': crontab(minute=schedule_minutes),  # Uses configurable schedule
    },
}
