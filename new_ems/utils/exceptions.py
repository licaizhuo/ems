from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status

from utils.response import MyResponse


def exception_handler(exc, context):
    error = "%s--%s--%s" % (context['view'], context['request'].method, exc)
    print(error)

    response = drf_exception_handler(exc, context)
    if response is None:
        return MyResponse(data_status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          data_message="程序内部错误，请稍等一会儿~", exception=None)
    return response
