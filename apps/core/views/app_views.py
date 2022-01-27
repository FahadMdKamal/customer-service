# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from apps.core.models import App

# from apps.core.serializers import AppSerializer


# class AppsListView(APIView):
    
#     def get(self, request):
#         apps = App.objects.all()
#         serializer = AppSerializer(apps, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
