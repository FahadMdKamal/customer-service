from django.http import HttpResponse
import json
from mods.webhook.models import Ticket
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist


class TicketUpdateView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))

        if "ref_id" in data:
            ref_id = data["ref_id"]
        else:
            return HttpResponse("Ref id is required.")

        if "case_id" in data:
            case_id = data["case_id"]
        else:
            return HttpResponse("Case id is required.")

        try:
            ticket = Ticket.objects.get(id=ref_id)
            ticket.case_id = case_id
            ticket.save()
        except ObjectDoesNotExist:
            pass

        return HttpResponse(status=200)
