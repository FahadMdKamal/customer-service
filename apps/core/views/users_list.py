from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.core.serializers import UserSerializers, UserMiniSerializers
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated

from apps.core.utils.api_response_decorator import decorate_response

User = get_user_model()

class UserActivationApiView(APIView):

    def post(self, request, format='json'):

        if request.data.get('user_id', None):
            db_obj = get_object_or_404(User,id=request.data.get('user_id'))
            serializer = UserSerializers(db_obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return decorate_response(True,status.HTTP_202_ACCEPTED, "User Activated", serializer.data)
            else:
                return decorate_response(False,status.HTTP_400_BAD_REQUEST, "User Activation Faild")
        return decorate_response(False,status.HTTP_400_BAD_REQUEST, "User-id missing")



    # def post(self, request):
    #     if request.data.get('user_id'):
    #         # user_obj = get_object_or_404(User,id=request.data.get('user_id'))
    #         # user_obj.is_active=True
    #         # user_obj.save()
    #         return decorate_response(True,status.HTTP_202_ACCEPTED, "User Activated", UserSerializers(user_obj).data)

    #     return decorate_response(False,status.HTTP_400_BAD_REQUEST, "User Activation Faild")


class UserListApiView(APIView):
    permission_classes = [IsAuthenticated]

    
    def get(self, request, format=None):
        params = {}

        if self.request.query_params.get("user-group", None) is not None:
            params.update({"groups__name": self.request.query_params["user-group"]})
        
        obj_list = User.objects.filter(**params).order_by('-id')
        data = []
        nextPage = 0
        previousPage = 0
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)
        paginator = Paginator(obj_list, limit)
        try:
            data = paginator.page(page)
        except ObjectDoesNotExist:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = UserMiniSerializers(data, context={'request': request}, many=True)


        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response(
                {'data': serializer.data,
                 'count': paginator.count,
                 'total_pages': paginator.num_pages,
                 'next': nextPage,
                 'prev': previousPage,
                 'limit': limit}, 
                 status=status.HTTP_200_OK)
