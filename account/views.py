from django.contrib.auth import get_user_model
from .seralizers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        print(data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("You've been successfully registered", status=status.HTTP_201_CREATED)

