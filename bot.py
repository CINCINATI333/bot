import vk_api
vk = vk_api.VkApi(token="62c86307e99237c7e583214fc442b5bf48b7b0859c3f2b7e95977e26fc1f5f6ad18d07d2651763728edf0")
while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["text"]
        body = messages["items"][0]["last_message"]["text"]
        if body.lower() == "омаева му":
            vk.method("messages.send", {"peer_id":"id", "message":"шиндейру!"})
        else:
            vk.method("messages.send", {"peer_id":"id", "message":"NANI!!!"})
            mvrekgker

