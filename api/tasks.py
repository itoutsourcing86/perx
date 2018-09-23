from __future__ import absolute_import, unicode_literals
from .models import Key
from celery import task
from .utils import create_random_key


@task
def generate_keys_task():
    if Key.objects.filter(status=0).count() < 50:
        for i in range(100):
            create_random_key()
