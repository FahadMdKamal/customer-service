from django.http import HttpResponse
import json
from mods.webhook.models import Page, Ticket
from rest_framework.views import APIView
import threading
import requests
from django.core.exceptions import ObjectDoesNotExist
from config.settings import APP_URL
from config.settings import CASEX_URL


def throw_to_casex(app_token, event, action, ref_id, body_parsed):
    url = CASEX_URL + "/casex/webhook"
    querystring = {}
    headers = {"Content-Type": "application/json"}

    payload = {
        "app_token": app_token,
        "event": event,
        "action": action,
        "data": {
            "ref_id": ref_id,
            "body": body_parsed
        },
        "callback_url": APP_URL + "/webhook/ticketupdate/",
        "callback_ttl": "30"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    print('THROW', response.status_code, response.text)


def process_fb_feed_data(page_id, post_data):
    from_id = post_data['value']['from']['id']
    from_name = post_data['value']['from']['name']
    message = post_data['value']['message']
    item = post_data['value']['item']
    created_time = post_data['value']['created_time']
    content_id = ""

    if item == 'comment':
        content_id = post_data['value']['comment_id']
    elif item == 'post':
        content_id = post_data['value']['post_id']
    
    body_parsed = {
        "platform": "facebook",
        "source": page_id,
        "message_type": item,
        "content_id": content_id,
        "content": message,
        "from_type": 'psid',
        "from_ref": from_id,
        "from_name": from_name,
        "received_at": created_time
    }

    try:
        ticket = Ticket.objects.get(platform='facebook', source=page_id, content_id=content_id, from_type='psid', from_ref=from_id, received_at=created_time)
    except ObjectDoesNotExist:
        ticket = Ticket(
            message_type=item,
            platform='facebook',
            source=page_id,
            content_id=content_id,
            body=post_data,
            body_parsed=json.dumps(body_parsed),
            from_type='psid',
            from_ref=from_id,
            from_name=from_name,
            received_at=created_time,
            status='open'
        )
        ticket.save()

    t = threading.Thread(target=throw_to_casex, args=["029348320", item, "incoming", ticket.id, body_parsed], daemon=True)
    t.start()


def process_fb_message_data(page_id, post_data):
    from_id = post_data[0]['sender']['id']
    from_name = ''
    message = post_data[0]['message']['text']
    item = 'messaging'
    created_time = post_data[0]['timestamp']
    content_id = post_data[0]['message']['mid']
    
    body_parsed = {
        "platform": "facebook",
        "source": page_id,
        "message_type": item,
        "content_id": content_id,
        "content": message,
        "from_type": 'psid',
        "from_ref": from_id,
        "from_name": from_name,
        "received_at": created_time
    }

    try:
        ticket = Ticket.objects.get(platform='facebook', source=page_id, message_type=item, content_id=content_id, from_type='psid', from_ref=from_id, received_at=created_time)
    except ObjectDoesNotExist:
        ticket = Ticket(
            message_type=item,
            platform='facebook',
            source=page_id,
            content_id=content_id,
            body=post_data,
            body_parsed=json.dumps(body_parsed),
            from_type='psid',
            from_ref=from_id,
            from_name=from_name,
            received_at=created_time,
            status='open'
        )
        ticket.save()

    t = threading.Thread(target=throw_to_casex, args=["029348320", item, "incoming", ticket.id, body_parsed], daemon=True)
    t.start()


class FacebookWebhookView(APIView):
    def get(self, request):
        VERIFY_TOKEN = "SECRET"

        if request.GET["hub.verify_token"] == VERIFY_TOKEN:
            return HttpResponse(request.GET["hub.challenge"])
        else:
            return HttpResponse("Invalid verification token")

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        page_id = data["entry"][0]["id"]

        try:
            page = Page.objects.get(page_id=page_id, source='facebook')

            if 'messaging' in data['entry'][0]:
                message_data = data['entry'][0]['messaging']
                t = threading.Thread(target=process_fb_message_data,args=[page_id, message_data],daemon=True)
                t.start()

            elif 'changes' in data['entry'][0]:
                post_data = data['entry'][0]['changes'][0]

                from_id = int(post_data['value']['from']['id'])
                item = post_data['value']['item']
                
                if from_id > 0 and from_id != int(page_id) and item in ['post', 'comment']:
                    t = threading.Thread(target=process_fb_feed_data, args=[page_id, post_data], daemon=True)
                    t.start()

        except ObjectDoesNotExist:
            pass

        return HttpResponse(status=200)

