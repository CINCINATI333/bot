import vk_api
import random
import time

'''
vk = vk_api.VkApi(token="b0dc785bab967bfe0c04563e5648bc422c1ae6ceeba4341f16d386616ff73365afe85bd7e513eebde0954")
while True:
messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["text"]
        body = messages["items"][0]["last_message"]["text"]
        if body.lower() == "омаева му":
            vk.method("messages.send", {"peer_id":"id", "message":"шиндейру!"})
        else:
            vk.method("messages.send", {"peer_id":"id", "message":"NANI!!!"})
'''

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


