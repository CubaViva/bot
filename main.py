# -*- coding: cp1251 -*-
import requests
import fake_useragent
from bs4 import BeautifulSoup
import threading, time
import random
from collections import Counter


session = requests.Session()
apeha = "https://kovcheg2.apeha.ru/"
link = "https://kovcheg2.apeha.ru/index.shtml"
user = fake_useragent.UserAgent().random
header = {
    'user-agent': user
}
data = {
    'actUser-Login': '1',
    'login': 'CubaDaleko',
    'pwd' : 'kojlbt11'
}
def vremia ():
    t = time.localtime() 
    current_time = time.strftime("%H:%M:%S", t) 
    print(current_time)

responce = session.post(link, data=data, headers=header).text

src_start = responce.find("newWin")
src_end = responce.find("\"",src_start)
src_tri = responce.find("\"",src_end+1)
src = ""
for n in range(src_end + 1, src_tri):
    src = src + responce[n]
# link_magshop = "https://kovcheg2.apeha.ru/mageshop.html"
# link_cuba = "https://kovcheg2.apeha.ru/magiccasters.html"
link_newwin = str((src))
enter_responce = session.get(link_newwin, headers=header).text

# маг магаз
def mag_magaz ():
    link_magshop = "https://kovcheg2.apeha.ru/mageshop.html"
    responce = session.get(link_magshop, headers=header).text
    return responce
    print("Перешли в маг магаз")
    time.sleep(random.randint(1, 3))

# данные для посылки входа в алтарь Куба
cuba = {
    'unick': 'CubaDaleko'
}
# Куба заклинатель переход
def mag_cuba ():
    link_cuba = "https://kovcheg2.apeha.ru/magiccasters.html"
    responce = session.post(link_cuba, data=cuba, headers=header).text
    return responce
    print("Перешли в алтарь Куба")
    time.sleep(random.randint(1, 3))
# пока оставим но возможно можно будет удалить
cubamag_responce = mag_cuba()



def work (responce):
    src_cp = responce.find("Работать")
    return src_cp

def work_start (responce):
    src_cp = responce.find("Работать")
    src_cp_start = responce.find("\'m", src_cp)
    return src_cp_start

def work_end (responce):
    src_cp = responce.find("Работать")
    src_cp_start = responce.find("\'m", src_cp)
    src_cp_end = responce.find("\'", src_cp_start + 1)
    return src_cp_end


src_if = ""
for n in range(work(mag_cuba()), work(mag_cuba()) + 8):
    src_if = src_if + cubamag_responce[n]
m = 0

while src_if == "Работать":
    cubamag_responce = mag_cuba()

    src_if = ""
    for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
        src_if = src_if + cubamag_responce[n]
    src_1 = ""
    for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
        src_1 = src_1 + cubamag_responce[n]

    link_work = apeha + src_1
    work_responce = session.get(link_work, headers=header).text

    src_2 = ""
    src_rab = src_1.find(".")
    for n in range(0, src_rab):
        src_2 = src_2 + src_1[n]

    src_3 = ""
    src_wait = work_responce.find("Осталось отдыхать")
    src_time = work_responce.find(":", src_wait)
    for n in range(src_time + 6, src_time + 13):
        src_3 = src_3 + work_responce[n]
    print(src_3)

    src_data_work = ""
    src_rab_data = src_1.find("reqid")
    for n in range(src_rab_data + 6, src_rab_data + 14):
        src_data_work = src_data_work + src_1[n]
    work_data = {
        'jobid': src_data_work,
        'actUser-StartWork' : '42'
    }
    src_work = ""
    if src_wait == -1:
        print("Заебумба можно работать")
        link_back = apeha + src_2 + ".html"
        back_responce = session.post(link_back, data=work_data, headers=header).text      
        time.sleep(random.randint(10, 25))
        # маг магаз
        mag_responce = mag_magaz()
        time.sleep(random.randint(4, 13))
        cubamag_responce = mag_cuba()

        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print("Заебумба отработал дальше отдых: " + src_3)  
    else:
        print(src_3)
        print(src_1)
        print("Ждем 1,5 часа")
        vremia()
        time.sleep(random.randint(502, 590))
        print(src_3)  
    
        cubamag_responce = mag_cuba()

        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        src_altar = ""
        src_altar = cubamag_responce.find("Выберите предмет")
        src_altar_start = cubamag_responce.find("e=", src_altar+16)
        print(src_altar_start)


        work_responce = session.get(link_work, headers=header).text
        time.sleep(random.randint(5, 9))

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

# кладем на алтарь
        altar = ""
        for n in range(src_altar_start + 3, src_altar_start + 12):
            altar = altar + cubamag_responce[n]
        print(altar)
        print("Кладем шмотку на алтарь")
        altar_data = {
            'itemid': altar
        }       
        link_work = apeha + src_2 + ".html"
        print(link_work)
        altar_responce = session.post(link_work, data=altar_data, headers=header).text
# закончили класть

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("500 сек прошло")
        vremia()       
        time.sleep(random.randint(2081, 2119))
        cubamag_responce = mag_cuba()

        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("еще 45 минут")
        vremia()       
        time.sleep(random.randint(515, 545))
        print("еще 25 минут")
        vremia()       
        time.sleep(random.randint(1099, 1122))  
        print("еще 12 минут")
        vremia()       
        time.sleep(random.randint(1455, 1499))
        cubamag_responce = mag_cuba()

        src_if = ""
        for n in range(work(cubamag_responce), work(cubamag_responce) + 8):
            src_if = src_if + cubamag_responce[n]
        src_1 = ""
        for n in range(work_start(cubamag_responce) + 1, work_end(cubamag_responce)):
            src_1 = src_1 + cubamag_responce[n]

        link_work = apeha + src_1
        work_responce = session.get(link_work, headers=header).text

        src_2 = ""
        src_rab = src_1.find(".")
        for n in range(0, src_rab):
            src_2 = src_2 + src_1[n]

        src_3 = ""
        src_wait = work_responce.find("Осталось отдыхать")
        src_time = work_responce.find(":", src_wait)
        for n in range(src_time + 6, src_time + 13):
            src_3 = src_3 + work_responce[n]
        print(src_3)
        print("проверка работы")  
    vremia()        
    m += 1
    print("Круг" + str(m))