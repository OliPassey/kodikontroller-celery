from celery import Celery
from .config import CeleryConfig

def make_celery():
    celery = Celery(__name__)
    celery.config_from_object(CeleryConfig)
    return celery

celery = make_celery()
