from rest_framework.response import Response

def decorate_response(serializer_data, status:bool, status_code, message) -> Response:
    return Response({
        'status': "success" if status else "faild" ,
        'message': message,
        'data': serializer_data
    }, status=status_code)