# scraper/serializers.py
from rest_framework import serializers
from .models import ScrapingJob, ScrapingTask

class ScrapingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapingTask
        fields = ['coin', 'status', 'output']

class ScrapingJobSerializer(serializers.ModelSerializer):
    tasks = ScrapingTaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = ScrapingJob
        fields = ['job_id', 'created_at', 'tasks']
