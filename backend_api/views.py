from django.shortcuts import render
from rest_framework.views import APIView
from .models import People
from .serializer import PeopleSerializer
from rest_framework.response import Response


class PeopleAPIView(APIView):
    def get(self, request):
        output = [
            {
                "name": output.name,
                "last_name": output.last_name,
                "age": output.age
            } for output in People.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
