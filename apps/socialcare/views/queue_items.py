from apps.core.models import MavrikApps, MaverikChannels
from rest_framework.response import Response
from rest_framework.views import APIView
from mods.queue_service.models import QueueItems
from apps.socialcare.serializers import QueueItemsSerializer
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status


class QueueItemList(APIView):

    serializer_class = QueueItemsSerializer

    def get(self, request):

        params = {}

        if request.query_params.get("app-id", None) is not None:
            params.update({"id": request.query_params["app-id"]})

        obj_list = QueueItems.objects.filter(**params).order_by("-id")
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

        serializer = QueueItemsSerializer(
            data, context={'request': request}, many=True)

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
                'messages': serializer.data,
            },
            status=status.HTTP_200_OK)
