# scraper/tasks.py
from celery import shared_task
from .models import ScrapingJob, ScrapingTask
from .coinmarketcap import CoinMarketCap

@shared_task
def scrape_coin_data(job_id, coin):
    job = ScrapingJob.objects.get(job_id=job_id)
    task = ScrapingTask.objects.create(job=job, coin=coin)

    scraper = CoinMarketCap(coin)
    data = scraper.scrape_data()

    if data:
        task.status = 'completed'
        task.output = data
    else:
        task.status = 'failed'
    task.save()
