from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """TEST API VIEW"""

    def get(self, request, format=None):
        """returns a list of features"""
        an_apiview = [
            "uses http methods as functions",
            "is similar to traditional django",
            "gives most control over application logic",
            "is mapped manually to urls",
        ]
        return Response({"message": "Hello", "data": an_apiview})
