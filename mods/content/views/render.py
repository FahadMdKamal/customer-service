from rest_framework.views import APIView
from rest_framework import response
import json
import datetime

'''
[{"key": "today", "default": "jani na", "value_resolver": "func_date_today"}]
'''


class MCLS:

    @staticmethod
    def func_date_today():
        return str(datetime.datetime.today())


# value_resolver = value_resolver()

class RenderView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))

        print(data)
        if 'value_resolver' in data:
            value_resolver = data['value_resolver']
            value = getattr(MCLS, value_resolver)()
        else:
            value = data['default']

        return response.Response({data['key']: value})
