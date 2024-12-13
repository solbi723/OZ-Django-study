from django.shortcuts import render
from .models import Review
from .serializer import ReviewSerializer
from rest_framework.response import Response 
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

# Create your views here.
# api/v1/reviews [GET]
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews,many=True)
        return Response(serializer.data)
        

# api/v1/reviews/reviews_id [GET]
class ReviewDetail(APIView):
    def get(self, request,review_id):
        try:
            review = Review.objects.get(id=review_id)
        except:
            raise NotFound
        
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
