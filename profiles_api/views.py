# from django.shortcuts import render
#
# # Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Naeem Ahmed',
            'Nayon Ahmed',
            'Sadik',
        ]
        return Response({'message':'Hello!', 'an_apiview': an_apiview})
