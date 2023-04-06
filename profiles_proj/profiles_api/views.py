from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializer


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
