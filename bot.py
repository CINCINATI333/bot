import vk_api
import random
import time
import xlwt
import xlrd
from xlutils.copy import copy
from openpyxl import load_workbook


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
        rb = xlrd.open_workbook('1.xlsx')

        wb = copy(rb)

        w_sheet = wb.get_sheet(0)

        w_sheet.write(0,0,text[0]) #Проба записи в ячейку (0,1) первого элемента сообщения
        w_sheet.write(0,1,text[1])
        a = abs(int(text[3])-int(text[2])) #Считается разность между 4 и 3 числами в сообщении
        w_sheet.write(0,2,a) #Разность записывается в ячейку
        

        wbook = xlrd.open_workbook('1.xls') #Открыл файл Excel
        wsheet = wbook.sheet_by_index(0) #открыл первый лист
        a = int(wsheet.cell(0,0).value) #записал в переменную значение ячейки A1
        
    
        
        wb.save('1.xls')


    time.sleep( 1 )
