from django.shortcuts import render
from rest_framework import generics
from .serializers import PlayerStatSerializer
from .models import PlayerStats

class RequestLogMiddleware(object):
    def initial(self, request, *args, **kwargs):
         super(RequestLogMiddleware, self).initial(request, *args, **kwargs)
         print(request.method)
         print(request.body)
         print(request.META["CONTENT_TYPE"])

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset=PlayerStats.objects.all()
    serializer_class=PlayerStatSerializer

    def perform_create(self,serializer):
        serializer.save()