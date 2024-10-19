# tasks.py en alguna de tus apps de Django

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_task_creation_email(task_title, recipient_email):
    send_mail(
        'Nueva Tarea Creada',
        f'Se ha creado una nueva tarea: {task_title}',
        'jesusalayond@gmail.com',  
        [recipient_email]
    )