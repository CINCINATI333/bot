  
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
while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
    if messages and messages["count"]:
        id = messages["items"][0]["conversation"]["peer"]["id"] #Получили ID приславшего сообщение 
        text = messages["items"][0]["last_message"]["text"] #Записали  переменную текст сообщения   
        
        uid = id
        fields = "first_name, last_name"
        res = vk.method("users.get", {"user_ids": uid, "fields": fields })
        user = { 'name': 'xname', 'surname': 'xsurname' }
        uname = res[0]['first_name'] #Записали в переменную имя пользователя
        ulastname = res[0]['last_name'] #Записали в переенную фамилию пользователя

        if text.lower() == "омае ва му":
            vk.method("messages.send", {"peer_id": id, "message":"шиндейру!", "random_id": get_rand()})
        else:
            vk.method("messages.send", {"peer_id": id, "message":"Nein!!!!", "random_id": get_rand()})  
        text = text.split() #Разбили текст сообщения на массив
        print(text)
        try:
            match = str(text[0])
            score1 = str(text[1])
            score2 = str(text[2])
        except():
            print( "Wrong line syntax!" )
            vk.method("messages.send", {"peer_id": id, "message":"Нипральна! Широкую на широкую!", "random_id": get_rand()})
            continue
       
        unumber = 4 #Разница в количестве столбцов между ячейками с номерами матчей
        wbook = xlrd.open_workbook('2.xls') #Открыл файл Excel
        wb = copy(wbook)
        w_sheet = wb.get_sheet(0) #открыл первый лист
        w_sheet2 = wbook.sheet_by_index(0) #Открыл первый лист другим методом (другой библиотекой)
        b = float(w_sheet2.cell(0,0).value)
        print(b)

        match=match+'.0'
        a = [0 for i in range(1,100)]
        k=0
        i=1
        while i<30:
            a[i] = str(w_sheet2.cell(0,int(i)).value) #записть в переменную данных с 1-ой строки экселя (строка, столбец)
            if a[i] == match: #если значение в 1 строке столбца i равно переменной match (присланноый номер мачта)
                k=i
                unumber = float(b)+4 #номер строки, в первом столбце которой будет имя и фамилия пользователя
                w_sheet.write(0,0,float(b)+1) #Запись в ячейку количества пользователей, отправивших сообщения
                b+=1
            i+=1
        
        w_sheet.write(unumber,k+2,text[1]+ '-' + text[2]) #запись счёта
        w_sheet.write(unumber,0,uname +' '+ ulastname) #запись имени и фамилии
        w_sheet.write(0,0 ,b) #запись количества пользователей, приславших сообщение
        wb.save('2.xls')

        
        print(res[0]['first_name']) #Имя
        print(res[0]['last_name']) #Фамилия

        print(text[0],'  - первый элемент сообщения')
        print(text[1], ' - второй элемент сообщения')
        print(text[2], ' - третий элемент сообщения')
          
        

    time.sleep( 3 )
