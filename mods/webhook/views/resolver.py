from django.http import HttpResponse
import json
from mods.webhook.models import Page, Ticket
from rest_framework.views import APIView
import threading
import requests
from django.core.exceptions import ObjectDoesNotExist


def process_fb_post_comment_reply(ticket_id, source, reply_message_type, content_id, content):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except ObjectDoesNotExist:
        return HttpResponse("Ticket information not found.")

    try:
        page = Page.objects.get(page_id=source)
    except ObjectDoesNotExist:
        return HttpResponse("Page information not found.")

    access_token = page.page_access_token

    url = "https://graph.facebook.com/v12.0/" + str(content_id) + "/comments"
    querystring = {"access_token": access_token}
    payload = {
        "message": content
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    if response.status_code == 200:
        ticket.status = 'closed'
        ticket.save()
        print(response.status_code, "SUCCESS", response.text)
    else:
        print(response.status_code, "ERROR", response.text)


def process_fb_message_reply(ticket_id, source, reply_message_type, content_id, content):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except ObjectDoesNotExist:
        return HttpResponse("Ticket information not found.")

    try:
        page = Page.objects.get(page_id=source)
    except ObjectDoesNotExist:
        return HttpResponse("Page information not found.")

    access_token = page.page_access_token

    print(source, content_id, reply_message_type, content, access_token)

    url = "https://graph.facebook.com/v12.0/me/messages"
    headers = {"Content-Type": "application/json"}
    querystring = {"access_token": access_token}
    payload = {
        "messaging_type": "RESPONSE",
        "recipient": {
            "id": ticket.from_ref
        },
        "message": {
            "text": content
        }
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    if response.status_code == 200:
        ticket.status = 'closed'
        ticket.save()
        print(response.status_code, "SUCCESS", response.text)
    else:
        print(response.status_code, "ERROR", response.text)


class ResolverWebhookView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if "ticket_id" in data:
            ticket_id = data["ticket_id"]

            try:
                ticket = Ticket.objects.get(id=ticket_id)
            except ObjectDoesNotExist:
                return HttpResponse("Ticket information not found.")
        else:
            return HttpResponse("Ticket id is required.")

        if "content" in data:
            content = data["content"]
        else:
            return HttpResponse("Reply content is required.")

        if "reply_message_type" in data:
            reply_message_type = data["reply_message_type"]
            if reply_message_type not in ["comment", "private_reply", "messaging", "delete", "comment_reaction"]:
                return HttpResponse("Reply message type not found.")
        else:
            return HttpResponse("Reply message type is required.")

        print(ticket.source, reply_message_type, ticket.content_id, content)

        if reply_message_type in ["comment", "comment_reaction"]:
            t = threading.Thread(target=process_fb_post_comment_reply,
                                 args=[ticket_id, ticket.source, reply_message_type, ticket.content_id, content],
                                 daemon=True)
            t.start()
        elif reply_message_type in ["messaging", "private_reply"]:
            t = threading.Thread(target=process_fb_message_reply,
                                 args=[ticket_id, ticket.source, reply_message_type, ticket.content_id, content],
                                 daemon=True)
            t.start()

        try:
            pass
        except ObjectDoesNotExist:
            pass

        return HttpResponse(status=200)
