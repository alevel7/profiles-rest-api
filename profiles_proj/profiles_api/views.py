from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializer
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """TEST API VIEW"""

    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """returns a list of features"""
        an_apiview = [
            "uses http methods as functions",
            "is similar to traditional django",
            "gives most control over application logic",
            "is mapped manually to urls",
        ]
        return Response({"message": "Hello", "data": an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """update an exising"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """partial update an exising"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """delete an exising"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test api view set"""

    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """returns a hello message"""
        a_viewset = [
            "uses http methods as functions",
            "is similar to traditional django",
            "gives most control over application logic",
            "is mapped manually to urls",
        ]
        return Response({"message": "Hello", "data": a_viewset})

    def create(self, request):
        "creates new obj"
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """handle getting an object by id"""
        return Response({"method": "GET"})

    def update(self, request, pk=None):
        """handle updating an object by id"""
        return Response({"method": "UPDATE"})

    def partial_update(self, request, pk=None):
        """handle partially updating part of an object by id"""
        return Response({"method": "PARTIAL]"})

    def destroy(self, request, pk=None):
        """handle deleting an object by id"""
        return Response({"method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handles creating and updating profiles"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = (
        "name",
        "email",
    )
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handles creating , reading, updating profile feed items"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, permissions.UpdateOwnStatus]
    serializer_class = serializer.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
