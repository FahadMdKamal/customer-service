from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenVerifyView
)


class TokenValidationAPIView(TokenVerifyView):

    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)
        if resp.status_code == 200:
            resp.data['status'] = True
            resp.data['message'] = "Valid Token"
        return Response(resp.data, status=status.HTTP_200_OK)
