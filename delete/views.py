from django.shortcuts import render

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscriber
from .serializers import subscriberSerializer


# Create your views here.
class subscriberList(APIView):

    def get(self, request):
        #subscriber1 = Subscriber.objects.all()
        #subscriber1 = Subscriber.objects.raw("SELECT * FROM subscriber;")
        #subscriber1 = Subscriber.objects.raw("DELETE  FROM subscriber WHERE LENGTH(username)>5;")
        subscriber1 = Subscriber.objects.raw("DELETE  FROM subscriber WHERE id>5;")
        serializer = subscriberSerializer(subscriber1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
# Create your views here.
