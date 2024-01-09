import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')

app = Celery('djangoProject1')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'update-resources-every-10-seconds': {
        'task': 'plemiona.tasks.update_resources',
        'schedule': 10.0,  # wykonuje się co 10 sekund
    },
    'check-building-tasks-every-second': {
        'task': 'plemiona.tasks.check_building_tasks',
        'schedule': 1.0,  # uruchamia co 1 sekundę
    },
    'check-process_attacks-tasks-every-second': {
        'task': 'plemiona.tasks.process_attacks',
        'schedule': 1.0,  # uruchamia co 1 sekundę
    },
    'check_research_tasks-tasks-every-second': {
        'task': 'plemiona.tasks.check_research_tasks',
        'schedule': 1.0,  # uruchamia co 1 sekundę
    },
    # 'process_recruitment_orders-tasks-every-second': {
    #     'task': 'plemiona.tasks.process_recruitment_orders',
    #     'schedule': 1.0,  # uruchamia co 1 sekundę
    # },

}