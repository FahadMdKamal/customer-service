from rest_framework.response import Response

def decorate_response(serializer_data, status:bool, status_code, obj) -> Response:
    return Response({
        'status': "success" if status else "faild" ,
        'message': f'{obj} update ' + "success" if status else "faild" ,
        'data': serializer_data
    }, status=status_code)