from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage

from apps.core.utils.api_response_decorator import decorate_response
from apps.core.models import Channels
from apps.core.serializers import ChannelSerializers


class ChannelsApiView(APIView):
    """
    Customized API view for Create, Update, filter Channels.
    """

    def post(self, request, *args, **kwargs):
        """
        - If the request contains ID field for the Channel Object than It will update
        - Else will create new Object.
        """
        if request.data.get('id'):
            db_object = Channels.objects.get(id=request.data.get('id'))
            serializer = ChannelSerializers(db_object, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return decorate_response(status_code=status.HTTP_202_ACCEPTED,
                    status=True,
                    message="Channel Updated successfully",
                    serializer_data=serializer.data)
        else:
            serializer = ChannelSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return decorate_response(status_code=status.HTTP_201_CREATED,
                    status=True,
                    message="Channel Created successfully",
                    serializer_data=serializer.data)

        return  decorate_response(status_code=status.HTTP_400_BAD_REQUEST,
                    status=False,
                    message="Channel Operation Faild",
                    serializer_data=serializer.errors)
    
    def get(self, request):
        """
        Return List of channels if no params are given.
        If params (channel-id, channel-name, mailbox-id, mailbox-name) are given returns object(s) else null
        """

        params = {}

        if self.request.query_params.get("channel-id", None) is not None:
            params.update({"id": self.request.query_params["channel-id"]})

        if self.request.query_params.get("channel-name", None) is not None:
            params.update({"channel_name": self.request.query_params["channel-name"]})

        if self.request.query_params.get("mailbox-id", None) is not None:
            params.update({"mail_box_id": self.request.query_params["mailbox-id"]})

        if self.request.query_params.get("mailbox-name", None) is not None:
            params.update({"mail_box__name": self.request.query_params["mailbox-name"]})
        
        if params:
            db_object = Channels.objects.filter(**params)
            if db_object.count() > 0:
                serializer = ChannelSerializers(db_object, many=True)
                return decorate_response(status_code=status.HTTP_200_OK,
                    status=True,
                    message="Channel(s) Found",
                    serializer_data=serializer.data)
            else:  
                return decorate_response(status_code=status.HTTP_400_BAD_REQUEST,
                    status=False,
                    message="Channel(s) Not-Found",
                    serializer_data=[])
        else:
            obj_list = Channels.objects.all().order_by('-id')
            serializer = ChannelSerializers(obj_list, many=True)

            data = []
            nextPage = 1
            previousPage = 1
            page = request.GET.get('page', 1)
            limit = request.GET.get('limit', 10)
            paginator = Paginator(obj_list, limit)
            try:
                data = paginator.page(page)
            except ObjectDoesNotExist:
                data = paginator.page(paginator.num_pages)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)

            serializer = ChannelSerializers(data, context={'request': request}, many=True)


            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()

            return Response(
                    {'count': paginator.count,
                    'total_pages': paginator.num_pages,
                    'next': nextPage,
                    'prev': previousPage,
                    'limit': limit,
                    'data': serializer.data}, 
                    status=status.HTTP_200_OK)
                    

class ChannelDeleteApiView(APIView):

    def get(self, request):
        params = {}

        if self.request.query_params.get("channel-id", None) is not None:
            params.update({"id": self.request.query_params["channel-id"]})
        
        app = Channels.objects.filter(id=request.query_params.get('channel-id'))
        if app:
            app.delete()
            return decorate_response(status_code=status.HTTP_204_NO_CONTENT,
                    status=True,
                    message="Channel Deleted Successfully",
                    serializer_data=[])

        return decorate_response(status_code=status.HTTP_204_NO_CONTENT,
                status=False,
                message="App Deletion Faild",
                serializer_data=[])
