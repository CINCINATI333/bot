import vk_api
import random
import time
import xlwt


def get_rand():
  return random.random()*2*9223372036854775806 - 9223372036854775806

vk = vk_api.VkApi(token="62c86307e99237c7e583214fc442b5bf48b7b0859c3f2b7e95977e26fc1f5f6ad18d07d2651763728edf0")

uid = "254229781"
fields = "first_name, last_name"
res = vk.method("users.get", {"user_ids": uid, "fields": fields })

while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
    if messages and messages["count"]:
        id = messages["items"][0]["conversation"]["peer"]["id"]
        text = messages["items"][0]["last_message"]["text"]
        
        uid = id
        fields = "first_name, last_name"
        res = vk.method("users.get", {"user_ids": uid, "fields": fields })
        user = { 'name': 'xname', 'surname': 'xsurname' }
       
        #user = [ name: xname, surname: xsurname ]
        #print(xname)
       
        if text.lower() == "омае ва му":
            vk.method("messages.send", {"peer_id": id, "message":"шиндейру!", "random_id": get_rand()})
        else:
            vk.method("messages.send", {"peer_id": id, "message":"Nein!!!!", "random_id": get_rand()})  
        print(res[0]['first_name']) 
        print(res[0]['last_name'])
        text = text.split()
        print(text[0],'  - первый элемент сообщения')
        print(text[1], ' - второй элемент сообщения')
        print(text[2], ' - третий элемент сообщения')
        print(text[3], ' - четвёртый элемент сообщения')
        wb = xlwt.Workbook()
        ws = wb.add_sheet
        ws.write()

    time.sleep( 1 )
