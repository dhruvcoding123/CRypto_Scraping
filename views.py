# scraper/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScrapingJob, ScrapingTask
from .serializers import ScrapingJobSerializer
from .tasks import scrape_coin_data

class StartScrapingView(APIView):
    def post(self, request):
        coins = request.data.get('coins', [])
        if not all(isinstance(coin, str) for coin in coins):
            return Response({"error": "Invalid input, all elements must be strings"}, status=status.HTTP_400_BAD_REQUEST)

        job = ScrapingJob.objects.create()
        for coin in coins:
            scrape_coin_data.delay(job.job_id, coin)
        
        return Response({"job_id": job.job_id}, status=status.HTTP_202_ACCEPTED)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        try:
            job = ScrapingJob.objects.get(job_id=job_id)
        except ScrapingJob.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ScrapingJobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create your views here.
