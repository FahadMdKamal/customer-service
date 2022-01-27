from django.urls import path

urlpatterns = [
    # /livechat/queue/item_list?user_id=10&channel_id=10&queue_status=pending
    # /livechat/queue/item_list?user_id=10&channel_id=10&queue_status=disputed
    # /livechat/queue/item_list?user_id=10&channel_id=10&queue_status=active

    # /livechat/queue/item_ops?action=claim&queue_id=11011
    # /livechat/queue/item_ops?action=close&queue_id=11011
    # /livechat/queue/item_ops?action=transfer&target_user_id=11&queue_id=11011

]
