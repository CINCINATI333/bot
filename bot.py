import vk_api
import random
import time
import xlwt
import xlrd
from xlutils.copy import copy
from openpyxl import load_workbook

COLUMN_WIDTH = 4


def get_rand():
  return random.random()*2*9223372036854775806 - 9223372036854775806

#возвращает обработанную строку
def get_clear( str ):
    return str.lower().trim()

vk = vk_api.VkApi(token="62c86307e99237c7e583214fc442b5bf48b7b0859c3f2b7e95977e26fc1f5f6ad18d07d2651763728edf0")
column = 1

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

        try:
            team1 = text[0]
            team2 = text[1]
            score1 = text[2]
            score2 = text[3]
        except():
            print( "Wrong line syntax!" )
            vk.method("messages.send", {"peer_id": id, "message":"Нипральна! Широкую на широкую!", "random_id": get_rand()})
            continue

        #тут мы получили 4 слова team1 team2 score1 и score2
        #далее проверим являются ли команды 1 и 2 командами из списков
        team_check = [0,0,0,0]
        wbook = xlrd.open_workbook('1.xls') #Открыл файл Excel
        w_sheet = wbook.sheet_by_index(0) #открыл первый лист
        for k in range(1,10,2):
            team_check[k] = str(w_sheet.cell(0,k).value)
        print(team_check)
        '''
        team1_check = int(w_sheet.cell(0,int(column)).value) #записал в переменную значение ячейки B1
        team2_check = int(w_sheet.cell(0,int(column+2)).value) #записал в переменную значение ячейки D1
        team3_check = int(w_sheet.cell(0,int(column+4)).value) #записал в переменную значение ячейки F1
        team4_check = int(w_sheet.cell(0,int(column+6)).value) #записал в переменную значение ячейки H1
        team5_check = int(w_sheet.cell(0,int(column+8)).value) #записал в переменную значение ячейки
        team6_check = int(w_sheet.cell(0,int(column+10)).value) #записал в переменную значение ячейки 
        team7_check = int(w_sheet.cell(0,int(column+12)).value) #записал в переменную значение ячейки 
        team8_check = int(w_sheet.cell(0,int(column+14)).value) #записал в переменную значение ячейки 
        team9_check = int(w_sheet.cell(0,int(column+16)).value) #записал в переменную значение ячейки 
        team10_check = int(w_sheet.cell(0,int(column+18)).value) #записал в переменную значение ячейки 
        #valid = False   #if all right 
        k = 1
       
        valid = False
        for k in range(1,15,2):
            if get_clear(team1) == get_clear(team_check[k]):
                if get_clear(team2) == get_clear(team_check[k+2]):
                    #valid = True
                    rb = xlrd.open_workbook('1.xls')
                    wb = copy(rb)
                    w_sheet.write(0,k,team1) #Проба записи в ячейку (0,k) первого элемента сообщения
                    w_sheet.write(0,k+2,team2)
                    a = abs(int(team1)-int(team2)) #Считается разность между 4 и 3 числами в сообщении
                    w_sheet.write(0,2,a) #Разность записывается в ячейку
                    wb.save('1.xls')
                    vk.method("messages.send", {"peer_id": id, "message":"Принято!", "random_id": get_rand()})
                    valid = True
        if valid == False:
            print( "Wrong team!" )
            vk.method("messages.send", {"peer_id": id, "message":"Нипральна! Широкую на широкую!", "random_id": get_rand()})


        #тут мы имеем валидные тимы
      
        wbook = xlrd.open_workbook('1.xls') #Открыл файл Excel
        w_sheet = wbook.sheet_by_index(0) #открыл первый лист
        a = int(w_sheet.cell(0,int(k)).value) #записал в переменную значение ячейки A1
        
        rb = xlrd.open_workbook('1.xls')
        wb = copy(rb)
        w_sheet.write(0,k,uname + ulastname) #Проба записи в ячейку (0,k+1) первого элемента сообщения
        #w_sheet.write(0,k+1,text[1])
        a = abs(int(text[3])-int(text[2])) #Считается разность между 4 и 3 числами в сообщении
        w_sheet.write(0,2,a) #Разность записывается в ячейку
        
        wb.save('1.xls')

        
        print(res[0]['first_name']) #Имя
        print(res[0]['last_name']) #Фамилия

        print(text[0],'  - первый элемент сообщения')
        print(text[1], ' - второй элемент сообщения')
        print(text[2], ' - третий элемент сообщения')
        print(text[3], ' - четвёртый элемент сообщения')
        '''

    time.sleep( 1 )
