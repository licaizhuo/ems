from rest_framework import serializers, exceptions

from empapi.models import Employee


class EmpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        extra_kwargs = {
            "emp_name": {
                "max_length": 25,
                "min_length": 3,
                "error_messages": {
                    "max_length": "1员工名长度不能超过25",
                    "min_length": "1员工名长度不能低于2",
                }
            },

        }

    def validate_emp_name(self, value):
        if Employee.objects.filter(emp_name=value):
            raise exceptions.ValidationError("1员工已存在")
        return value

    def validate_salary(self, value):
        if not value:
            raise exceptions.ValidationError("1请输入正确的工资")
        decimals_int, decimals_float = str(value).split('.')
        if len(decimals_int) > 8 or len(decimals_float) > 2:
            raise exceptions.ValidationError("1请输入正确的工资")
        return value
