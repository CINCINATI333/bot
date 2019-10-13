import vk_api
import random
import time

def get_rand():
  return random.random()*2*9223372036854775806 - 9223372036854775806

vk = vk_api.VkApi(token="62c86307e99237c7e583214fc442b5bf48b7b0859c3f2b7e95977e26fc1f5f6ad18d07d2651763728edf0")
while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
    if messages and messages["count"]:
        id = messages["items"][0]["conversation"]["peer"]["id"]
        text = messages["items"][0]["last_message"]["text"]
        print(text)
        d = open('data.txt','a')
        d.write(text + '\n')
        d.close()
        if text.lower() == "омае ва му":
            vk.method("messages.send", {"peer_id": id, "message":"шиндейру!", "random_id": get_rand()})
        else:
            vk.method("messages.send", {"peer_id": id, "message":"Nein!!!!", "random_id": get_rand()})   
    time.sleep( 1 )


