from django.db import transaction

# Create your views here.
from rest_framework import status, exceptions
from rest_framework.viewsets import ViewSet

from userapi.models import User
from userapi.serializers import UserModelSerializer
from utils.response import MyResponse


class UserAPIView(ViewSet):

    def login(self, request, *args, **kwargs):
        username = request.query_params.get('username')
        password = request.query_params.get('password')
        user = User.objects.filter(username=username, password=password)
        # print(user)
        if user:
            return MyResponse(data_message="1", results={"username": username})
        return MyResponse(data_status=status.HTTP_422_UNPROCESSABLE_ENTITY, data_message="0")

    def register(self, request, *args, **kwargs):
        user_data = request.data
        if user_data.get('password') and (user_data.get('password') != user_data.get('con_password')):
            raise exceptions.ValidationError("两次密码不同")
        user_ser = UserModelSerializer(data=user_data)
        user_ser.is_valid(raise_exception=True)
        with transaction.atomic():
            user_ser.save()
            return MyResponse(data_message="1")
