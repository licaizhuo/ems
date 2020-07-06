from rest_framework import serializers, exceptions

from userapi.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "real_name", "password", "gender")
        extra_kwargs = {
            "username": {
                "max_length": 25,
                "min_length": 3,
                "error_messages": {
                    "max_length": "1用户名长度不能超过25",
                    "min_length": "1用户名长度不能低于3",
                }

            },
            "real_name": {
                "write_only": True,
                "max_length": 25,
                "min_length": 2,
                "error_messages": {
                    "max_length": "1用户名长度不能超过25",
                    "min_length": "1姓名长度不能低于",
                }
            },
            "password": {
                "write_only": True,
                "max_length": 25,
                "min_length": 3,
                "error_messages": {
                    "max_length": "1密码长度不能超过25",
                    "min_length": "1密码长度不能低于3",
                }
            },
        }

    def validate_username(self, value):
        if User.objects.filter(username=value):
            raise exceptions.ValidationError("1用户已存在")
        return value
