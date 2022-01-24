import string
from rest_framework.response import Response
from rest_framework import status

def decorate_response(status:bool, status_code:status, message: string, serializer_data=None) -> Response:
    return Response({
        'status': "success" if status else "faild" ,
        'message': message,
        'data': serializer_data
    }, status=status_code)