# from django.shortcuts import render
#
# # Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class HelloAPIView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = [
            'Naeem Ahmed',
            'Nayon Ahmed',
            'Sadik',
        ]
        return Response({'message':'Hello!', 'an_apiview': an_apiview})


    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello ' + name

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})