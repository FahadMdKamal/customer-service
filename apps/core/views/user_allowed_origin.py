from django.core.paginator import Paginator, EmptyPage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.core.models import UserAllowOrigin
from apps.core.serializers import UserAllowedOriginSerializers
from apps.core.utils.api_response_decorator import decorate_response


class UserAllowOriginCreateUpateView(APIView):

    def post(self, request, format='json'):

        if request.data.get('user', None):
            db_obj = UserAllowOrigin.objects.filter(user__id=request.data.get('user'))
            if db_obj.exists():
                serializer = UserAllowedOriginSerializers(db_obj.first(), data=request.data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return decorate_response(True, status.HTTP_202_ACCEPTED, "User Allow Origin Updated", serializer.data)
                else:
                    return decorate_response(False, status.HTTP_400_BAD_REQUEST, "User Allow Origin update faild", serializer.errors)
            else:
                serializer = UserAllowedOriginSerializers(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return decorate_response(True, status.HTTP_201_CREATED, "User Allow Origin Created", serializer.data)
                else:
                    return decorate_response(False, status.HTTP_400_BAD_REQUEST, "User Allow Origin creation faild", serializer.errors)

        return decorate_response(False, status.HTTP_400_BAD_REQUEST, "user field requires an id")


    def get(self, request):

        params = {}

        if self.request.query_params.get("app-id", None) is not None:
            params.update({"app__id": self.request.query_params["app-id"]})

        if self.request.query_params.get("user-id", None) is not None:
            params.update({"user__id": self.request.query_params["user-id"]})

        obj_list = UserAllowOrigin.objects.filter(**params).order_by("-id")
        data = []
        nextPage = 0
        previousPage = 0
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 100)
        paginator = Paginator(obj_list, limit)
        try:
            data = paginator.page(page)
        except UserAllowOrigin.DoesNotExist:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = UserAllowedOriginSerializers(data, context={'request': request}, many=True)


        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response(
                {
                 'count': paginator.count,
                 'total_pages': paginator.num_pages,
                 'next': nextPage,
                 'prev': previousPage,
                 'limit': limit,
                'data': serializer.data,
                 }, 
                 status=status.HTTP_200_OK)

