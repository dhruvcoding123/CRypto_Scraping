# crypto_scraper/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Crypto_Scrapper.settings')

app = Celery('Crypto_Scrapper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))