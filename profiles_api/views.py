# from django.shortcuts import render
#
# # Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers, models, permissions

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


class HelloViewsets(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewsets = [
            'View sets',
            'Naeem Ahmed',
            'Nayon Ahmed',
            'Sadik',
        ]

        return Response({'message':'Hello','ViewSet': a_viewsets})


    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_date.get('name')
            message = 'Hello ' + name

            return Response({'message':message, 'Name': name})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        return Response({'method':'Retrieve (Get)'})


    def update(self, request, pk=None):
        return Response({'method': 'Update (Put)'})


    def partial_updates(self, request, pk=None):
        return Response({'method': 'Partial Update (Patch)'})


    def destroy(self, request, pk=None):
        return Response({'method': 'Destryo (Delete)'})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES