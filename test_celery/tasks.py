from celery import shared_task
from .fun import calculation


@shared_task
def send_exam_invitation():
    print("shared_task called")
    #calculation()
