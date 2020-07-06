from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin

from empapi.models import Employee
from empapi.serializer import EmpModelSerializer
from utils.response import MyResponse


class EmpGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin,
                        UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        # return MyResponse(data_status=status.HTTP_200_OK, data_message="查询成功")
        if 'id' in kwargs:
            employees = self.retrieve(request, *args, **kwargs)
        else:
            employees = self.list(request, *args, **kwargs)
        return MyResponse(data_status=status.HTTP_200_OK, data_message="查询成功", results={"employees": employees.data})

    def post(self, request, *args, **kwargs):
        # print(request.data)
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
