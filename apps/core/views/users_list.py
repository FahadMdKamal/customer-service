from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.core.serializers import UserSerializers
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated


class UserListApiView(APIView):
    permission_classes = [IsAuthenticated]

    
    def get(self, request, format=None):
        obj_list = User.objects.all().order_by('-id')
        data = []
        nextPage = 1
        previousPage = 1
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)
        paginator = Paginator(obj_list, limit)
        try:
            data = paginator.page(page)
        except ObjectDoesNotExist:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = UserSerializers(data, context={'request': request}, many=True)


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
