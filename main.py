import schedule
from plyer import notification
import time
import webbrowser
#from datetime import datetime
import sys
import os
import pyautogui
import requests
import pyscreenshot

"""
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
a = current_time[0]+current_time[1]


    if int(a) > 15:
        #notifyme("CLASSES COMPLETED")
        pass
    else:
        #notifyme("PROGRAM RUNNING IN BACKGROUND")
        while True:
            schedule.run_pending()
            time.sleep(10)


def notifyme(reminder):
    notification.notify(
        title="ALERT!",
        message=reminder,
        timeout=180
    )
    # webbrowser.open("https://g09.tcsion.com/LX/home/show_my_communities?c_id=Sreenidhi-Institute-of-Science-Technology-14490&from=dashboard&current_community_id=Sreenidhi-Institute-of-Science-Technology-14490")
"""

def closing():
    print("runing")
    try:
        os.system('TASKKILL /f /IM chrome.exe')
    except:
        print("chrome already closed")
    time.sleep(3)
    webbrowser.open("https://www.google.com/")
    time.sleep(3)
    try:
        pyautogui.hotkey("alt","f")
        time.sleep(3)
        pyautogui.press('x')
    except:
        print("failed")
    time.sleep(2)
    


def removess():
    try:
        os.remove("C:/Users/Administrator/Desktop/temp.png")
    except:
        requests.post("https://api.telegram.org/bot1897765735:AAHEbgS2fniQjI1PQ7zHrNh7Bao1BjMLYFU/sendMessage?chat_id=-524640948&text='Unable to remove picture'")
    

def checking():
    try:
        os.remove("C:/Users/Administrator/Desktop/temp.png")
    except:
        print("Already removed")
    time.sleep(5)
    try:
        image = pyscreenshot.grab()
        image.save("C:/Users/Administrator/Desktop/temp.png")
        time.sleep(3)
        files = {'photo':open("C:/Users/Administrator/Desktop/temp.png","rb")}
        resp = requests.post("https://api.telegram.org/bot1897765735:AAHEbgS2fniQjI1PQ7zHrNh7Bao1BjMLYFU/sendPhoto?chat_id=-524640948",files=files)
        print("sent done:",resp.status_code)
        time.sleep(10)
        del image
        del files
        del resp
        removess()
    except:
        temp="Hey Mr.vishal,Unable to take screenshot please check manually"
        requests.post(f"https://api.telegram.org/bot1897765735:AAHEbgS2fniQjI1PQ7zHrNh7Bao1BjMLYFU/sendMessage?chat_id=-524640948&text={temp}")
       
    
        
def M2():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join M-II class soon")
    webbrowser.open("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-mathematics-iim-ii-7hc16-588-14490")
    checking()


def DC():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join DC class soon")
    webbrowser.open("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-data-communicationsdc-7cc57-640-14490")
    checking()


def DBMS():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join DBMS class soon")
    webbrowser.open(
        "https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-database-management-systemsdbms-7ec0-339-14490")
    checking()


def SEANDOOAD():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join SE & OOAD class soon")
    webbrowser.open(
        "https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-software-engineering-and-ooadseooad-908-14490")
    checking()


def DE():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join DE class soon")
    webbrowser.open("https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-digital-electronicsde-7cc55-443-14490")
    checking()


def CO():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join CO class soon")
    webbrowser.open(
        "https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-computer-organizationco-7d408-689-14490")
    checking()


def ESE():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join ESE class soon")
    webbrowser.open(
        "https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-environmental-science-and-ecologyese-794-14490")
    checking()


def CSLAB():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join CSLAB class soon")
    webbrowser.open(
        "https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-computer-aided-software-engineeringc-409-14490")
    checking()

def DBMSLAB():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join DBMSLAB class soon")
    webbrowser.open(
        "https://g09.tcsion.com/LX/home/home_page?c_id=btech-ii-it-d-database-management-systemsdbms-lab-938-14490")
    checking()


def TS():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join TS class soon")
    webbrowser.open(
        "https://g09.tcsion.com/LX/service/changecommurl?c_id=btech-ii-it-d-technical-seminar-iv-7f494-227-14490&orgid=14490")
    checking()

def COLAB():
    closing()
    time.sleep(3)
    #notifyme("Hey Mr.vishal,join CoLAB class soon")
    webbrowser.open(
        "https://g09.tcsion.com/LX/service/changecommurl?c_id=btech-ii-it-d-computer-organizationco-lab-7d475-154-14490&orgid=14490")
    checking()




# monday
schedule.every().monday.at("09:36").do(CO)
schedule.every().monday.at("10:28").do(M2)
schedule.every().monday.at("11:26").do(DBMS)
schedule.every().monday.at("12:26").do(SEANDOOAD)
schedule.every().monday.at("14:06").do(DBMSLAB)

# tuesday
schedule.every().tuesday.at("09:36").do(DC)
schedule.every().tuesday.at("10:26").do(SEANDOOAD)
schedule.every().tuesday.at("11:26").do(DE)
schedule.every().tuesday.at("12:28").do(ESE)
schedule.every().tuesday.at("14:10").do(M2)
schedule.every().tuesday.at("14:54").do(CO)
schedule.every().tuesday.at("15:46").do(DBMS)

# wednesday
schedule.every().wednesday.at("09:38").do(ESE)
schedule.every().wednesday.at("10:26").do(CO)
schedule.every().wednesday.at("11:28").do(M2)
schedule.every().wednesday.at("12:26").do(DBMS)
schedule.every().wednesday.at("14:06").do(SEANDOOAD)
schedule.every().wednesday.at("14:56").do(DE)
schedule.every().wednesday.at("15:46").do(DC)

# thursday
schedule.every().thursday.at("09:36").do(DE)
schedule.every().thursday.at("10:26").do(DC)
schedule.every().thursday.at("11:26").do(SEANDOOAD)
schedule.every().thursday.at("12:26").do(DBMS)
schedule.every().thursday.at("14:10").do(CSLAB)



# friday
schedule.every().friday.at("09:38").do(M2)
schedule.every().friday.at("10:45").do(CO)
schedule.every().friday.at("11:29").do(DBMS)
schedule.every().friday.at("12:38").do(DE)
schedule.every().friday.at("14:06").do(SEANDOOAD)
schedule.every().friday.at("14:56").do(DC)
schedule.every().friday.at("15:48").do(ESE)

# saturday
schedule.every().saturday.at("09:36").do(DC)
schedule.every().saturday.at("10:28").do(ESE)
schedule.every().saturday.at("11:26").do(CO)
schedule.every().saturday.at("12:28").do(M2)
schedule.every().saturday.at("14:06").do(DE)
schedule.every().saturday.at("14:56").do(TS)



if __name__ == '__main__':
    temp="Program started"
    print(temp)
    url = f"https://api.telegram.org/bot1897765735:AAHEbgS2fniQjI1PQ7zHrNh7Bao1BjMLYFU/sendMessage?chat_id=-524640948&text={temp}"
    requests.get(url)
    del temp
    while True:
            schedule.run_pending()
            time.sleep(10)
