from django.db import models
import uuid

class ScrapingJob(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

class ScrapingTask(models.Model):
    job = models.ForeignKey(ScrapingJob, related_name='tasks', on_delete=models.CASCADE)
    coin = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='pending')
    output = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
