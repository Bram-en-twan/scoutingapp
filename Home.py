from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.clock import Clock
from kivy.core.window import Window

from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget
from kivy.graphics.opengl import glFinish
from kivy.app import App
from time import time

from itertools import chain

from kivy.graphics.texture import Texture

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    group = ObjectProperty(None)
    
    def loginBtn(self):
        #if db.validate(self.email.text, self.password.text):
        import mysql.connector

        def Loop3(var1,var2,var3,var4):
            global mydb
            mydb = mysql.connector.connect(
            host="eu-cdbr-west-03.cleardb.net",
            user=var1,
            passwd=var2,
            database=var3
            )
            global mycursor
            mycursor = mydb.cursor()
            global groep2
            groep2 = var4
            #replace_line("Personal.txt",6,groep2+"\n")
            #loginscreen()
            r1 = "!22@3##$3343@234!22@3##$3343@234"
            r2 = "!22@3##$3343@234!22@3##$3343@234"
            r3 = "!22@3##$3343@234!22@3##$3343@234"
            r4 = "!22@3##$3343@234!22@3##$3343@234"
            r5 = "!22@3##$3343@234!22@3##$3343@234"
            r6 = "!22@3##$3343@234!22@3##$3343@234"
            r7 = "!22@3##$3343@234!22@3##$3343@234"
            r8 = "!22@3##$3343@234!22@3##$3343@234"
            r9 = "!22@3##$3343@234!22@3##$3343@234"
            r10 = "!22@3##$3343@234!22@3##$3343@234"
            r11 = "!22@3##$3343@234!22@3##$3343@234"
            r12 = "!22@3##$3343@234!22@3##$3343@234"
            global loginname
            loginname = self.email.text
            sql = f"SELECT wachtwoord FROM {groep2} WHERE naam = '{self.email.text}'"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for result in myresult:
                r1 = result[0]
                
            #sql = f"SELECT gebruiker FROM {groep2} WHERE naam = '{self.email.text}'"
            #mycursor.execute(sql)
            #myresult = mycursor.fetchall()
            #for result in myresult:
            #    r2 = result[0]
                
            if r1 == self.password.text and r1 != "!22@3##$3343@234!22@3##$3343@234":
                MainWindow.current = self.email.text
                self.reset()
                sm.current = "main"
            import threading
            import time
            def background():
                while True:
                    mydb.commit()
                    time.sleep(45)
            def foreground():pass
            b = threading.Thread(name='background', target=background)
            f = threading.Thread(name='foreground', target=foreground)
            b.start()
            f.start()

        if self.group.text == "Bevers ochtend" or self.group.text == "bevers ochtend" or self.group.text == "beversochtend":  Loop3("b73badccc28509","46e7ba9f","heroku_b6ccf5347f986b7", "beversochtend") 
        elif self.group.text == "Bevers middag" or self.group.text == "bevers middag":   Loop3("b8a6ec5dd4f831","26d0c1e2","heroku_f9c9ff2287354ae", "beversmiddag")    
        elif self.group.text == "Sionihorde" or self.group.text == "sionihorde":      Loop3("bd261e04c4f7ac","2646f655","heroku_6ddc7ca4fb6c487", "sionihorde")    
        elif self.group.text == "Shantihorde" or self.group.text == "shantihorde":     Loop3("bcf0fc9752adca","4433dfb8","heroku_3e38dc503c384ed", "shantihorde")   
        elif self.group.text == "Mowglihorde" or self.group.text == "mowglihorde":     Loop3("b53a91493bfae6","b0c77f1c","heroku_043cac3778e37ef", "mowglihorde")
        elif self.group.text == "Ekerstroep" or self.group.text == "ekerstroep":      Loop3("b20d36b9e64e9a","592a9017","heroku_72bce5d900dc0c4", "ekerstroep") 
        elif self.group.text == "Pmttroep" or self.group.text == "PMT"or self.group.text == "pmt" or self.group.text == "Pmt":        Loop3("bbb1086e05f46c","305a5102","heroku_936cbdf524a261e", "pmtgroep") 
        elif self.group.text == "Gaaientroep" or self.group.text == "gaaientroep":     Loop3("b0c7dad8c663d1","111e5841","heroku_53e06e5ae9e9597", "gaaientroep")  
        elif self.group.text == "Ea757" or self.group.text == "ea757":           Loop3("b9af828f2f4586","64cb70a1","heroku_1cb03cce5ef2216", "ea757")  
        elif self.group.text == "Ea595" or self.group.text == "ea595":           Loop3("bfbf8c292bd780","408b12a0","heroku_4f770db4c2019e5", "ea595") 
        elif self.group.text == "Stam1" or self.group.text == "stam1":           Loop3("b4e6692218c8bb","55c5369c","heroku_4e519908e65abd9", "stam1") 
        elif self.group.text == "Stam2" or self.group.text == "stam2":           Loop3("be0d90306e78fd","dd2610aa","heroku_1112b001d39794d", "stam2")
        else:
            pop = Popup(title='Invalid Login',
            content=Label(text='Groep is niet juist'),
            size_hint=(None, None), size=(400, 400))
            pop.open()
        #else:
        #    invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.group.text = ""
global yc
yc="Niet ik"
class MainWindow(Screen):
    def labels(week):
        import datetime
        now = datetime.datetime.now()
        d = f'{now.year}-W{week}'
        r = datetime.datetime.strptime(d + '-1', '%G-W%V-%u')
        r2 = datetime.datetime.strptime(d + '-7', '%G-W%V-%u')
        print(r,"|"+"|",r2)
        r4 = str(r); r5 = str(r2)
        if r4.endswith('00:00:00'):
            url1 = r4[:-8]
        if r5.endswith('00:00:00'):
            url2 = r5[:-8]
        url5 = url1[0] + url1[1] +  url1[2] +  url1[3]#Jaar 1
        url3 = url1[5] + url1[6]#maand 1
        url4 = url1[8] + url1[9]#dag 1
        url6 = url2[0] + url2[1] +  url2[2] +  url2[3]#Jaar 2
        url7 = url2[5] + url2[6]#maand 2
        url8 = url2[8] + url2[9]#dag 2
        r3 = url4 + "-" + url3 + "-" + url5 + " t/m " + url8 + "-" + url7 + "-" + url6 + f" (Week {week})"
        return r3
    import datetime
    my_date = datetime.date.today() # if date is 01/01/2018
    year, week_num, day_of_week = my_date.isocalendar()
    #print("Week #" + str(week_num) + " of year " + str(year))
        
    try:WeekLabel1 = labels(week_num);
    except: WeekLabel1 = ""
    try:WeekLabel2 = labels(week_num + 1);
    except: WeekLabel2 = ""
    try:WeekLabel3 = labels(week_num + 2);
    except: WeekLabel3 = ""
    try:WeekLabel4 = labels(week_num + 3);
    except: WeekLabel4 = ""
    try:WeekLabel5 = labels(week_num + 4);
    except: WeekLabel5 = ""
    try:WeekLabel6 = labels(week_num + 5);
    except: WeekLabel6 = ""
    try:WeekLabel7 = labels(week_num + 6);
    except: WeekLabel7 = ""
    try:WeekLabel8 = labels(week_num + 7);
    except: WeekLabel8 = ""
    try:WeekLabel9 = labels(week_num + 8);
    except: WeekLabel9 = ""
    try:WeekLabel10 = labels(week_num + 9);
    except: WeekLabel10 = ""
    try:WeekLabel11 = labels(week_num + 10);
    except: WeekLabel11 = ""
    try:WeekLabel12 = labels(week_num + 11);
    except: WeekLabel12 = ""
    try:WeekLabel13 = labels(week_num + 12);
    except: WeekLabel13 = ""
    try:WeekLabel14 = labels(week_num + 13);
    except: WeekLabel14 = ""
    try:WeekLabel15 = labels(week_num + 14);
    except: WeekLabel15 = ""
    try:WeekLabel16 = labels(week_num + 15);
    except: WeekLabel16 = ""
    try:WeekLabel17 = labels(week_num + 16);
    except: WeekLabel17 = ""
    try:WeekLabel18 = labels(week_num + 17);
    except: WeekLabel18 = ""
    try:WeekLabel19 = labels(week_num + 18);
    except: WeekLabel19 = ""
    try:WeekLabel20 = labels(week_num + 19);
    except: WeekLabel20 = ""
    try:WeekLabel21 = labels(week_num + 20);
    except: WeekLabel21 = ""
    try:WeekLabel22 = labels(week_num + 21);
    except: WeekLabel22 = ""
    try:WeekLabel23 = labels(week_num + 22);
    except: WeekLabel23 = ""
    try:WeekLabel24 = labels(week_num + 23);
    except: WeekLabel24 = ""
    try:WeekLabel25 = labels(week_num + 24);
    except: WeekLabel25 = ""
    try:WeekLabel26 = labels(week_num + 25);
    except: WeekLabel26 = ""
    try:WeekLabel27 = labels(week_num + 26);
    except: WeekLabel27 = ""
    try:WeekLabel28 = labels(week_num + 27);
    except: WeekLabel28 = ""
    try:WeekLabel29 = labels(week_num + 28);
    except: WeekLabel29 = ""
    try:WeekLabel30 = labels(week_num + 29);
    except: WeekLabel30 = ""
    try:WeekLabel31 = labels(week_num + 30);
    except: WeekLabel31 = ""
    try:WeekLabel32 = labels(week_num + 31);
    except: WeekLabel32 = ""
    try:WeekLabel33 = labels(week_num + 32);
    except: WeekLabel33 = ""
    try:WeekLabel34 = labels(week_num + 33);
    except: WeekLabel34 = ""
    try:WeekLabel35 = labels(week_num + 34);
    except: WeekLabel35 = ""
    try:WeekLabel36 = labels(week_num + 35);
    except: WeekLabel36 = ""
    try:WeekLabel37 = labels(week_num + 36);
    except: WeekLabel37 = ""
    try:WeekLabel38 = labels(week_num + 37);
    except: WeekLabel38 = ""
    try:WeekLabel39 = labels(week_num + 38);
    except: WeekLabel39 = ""
    try:WeekLabel40 = labels(week_num + 39);
    except: WeekLabel40 = ""
    try:WeekLabel41 = labels(week_num + 40);
    except: WeekLabel41 = ""
    try:WeekLabel42 = labels(week_num + 41);
    except: WeekLabel42 = ""
    try:WeekLabel43 = labels(week_num + 42);
    except: WeekLabel43 = ""
    try:WeekLabel44 = labels(week_num + 43);
    except: WeekLabel44 = ""
    try:WeekLabel45 = labels(week_num + 44);
    except: WeekLabel45 = ""
    try:WeekLabel46 = labels(week_num + 45);
    except: WeekLabel46 = ""
    try:WeekLabel47 = labels(week_num + 46);
    except: WeekLabel47 = ""
    try:WeekLabel48 = labels(week_num + 47);
    except: WeekLabel48 = ""
    try:WeekLabel49 = labels(week_num + 48);
    except: WeekLabel49 = ""
    try:WeekLabel50 = labels(week_num + 49);
    except: WeekLabel50 = ""
    try:WeekLabel51 = labels(week_num + 50);
    except: WeekLabel51 = ""
    try:WeekLabel52 = labels(week_num + 51);
    except: WeekLabel52 = ""
    try:WeekLabel53 = labels(week_num + 52);
    except: WeekLabel53 = ""
    
    WeekLabels = [f"{WeekLabel1}", f"{WeekLabel2}", f"{WeekLabel3}",f"{WeekLabel4}", f"{WeekLabel5}", f"{WeekLabel6}",f"{WeekLabel7}", f"{WeekLabel8}", f"{WeekLabel9}",f"{WeekLabel10}", f"{WeekLabel11}", f"{WeekLabel12}",f"{WeekLabel13}", f"{WeekLabel14}", f"{WeekLabel15}",f"{WeekLabel16}", f"{WeekLabel17}", f"{WeekLabel18}",f"{WeekLabel19}", f"{WeekLabel20}", f"{WeekLabel21}",f"{WeekLabel22}", f"{WeekLabel23}", f"{WeekLabel24}",f"{WeekLabel25}", f"{WeekLabel26}",f"{WeekLabel27}",f"{WeekLabel28}", f"{WeekLabel29}", f"{WeekLabel30}",f"{WeekLabel31}", f"{WeekLabel32}", f"{WeekLabel33}",f"{WeekLabel34}", f"{WeekLabel35}", f"{WeekLabel36}",f"{WeekLabel37}", f"{WeekLabel38}", f"{WeekLabel39}",f"{WeekLabel40}", f"{WeekLabel41}", f"{WeekLabel42}",f"{WeekLabel43}", f"{WeekLabel44}", f"{WeekLabel45}",f"{WeekLabel46}", f"{WeekLabel47}", f"{WeekLabel48}", f"{WeekLabel49}", f"{WeekLabel50}",f"{WeekLabel51}",f"{WeekLabel52}",f"{WeekLabel53}"]

    def spinner_clicked(self, value):
        print(value)
        global value2
        value2 = value
        print("value2 = ", value2)
        import re
        self.weeknumber2 = value2[:-1]
        print("self.weeknumber2 = ", self.weeknumber2)
        
        self.weeknumber = self.weeknumber2[+32:]
        print("self.weeknumber = ", self.weeknumber)
        #self.weeknumber = re.sub('[)]', '', self.weeknumber2)
        #self.weeknumber = re.sub('\D', '', value2)

        

        sql = f"SELECT opkomstbechrijving FROM {groep2}_opkomst WHERE regel = '{self.weeknumber}'"
        print("sql = ", sql)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for result in myresult:
            r3 = result[0]
            try:
                
                yc = r3.split(";");print(yc[0])#;T.delete('1.0', END);T.insert('1.0',yc[0]+"\n");T.insert('2.0',yc[1]+"\n");T.insert('3.0',yc[2]+"\n");T.insert('4.0',yc[3]+"\n");T.insert('5.0',yc[4]+"\n");T.insert('6.0',yc[5]+"\n");T.insert('7.0',yc[6]+"\n");T.insert('8.0',yc[7]+"\n");T.insert('9.0',yc[8]+"\n");T.insert('10.0',yc[9]+"\n");T.insert('11.0',yc[10]+"\n");T.insert('12.0',yc[11]+"\n");T.insert('13.0',yc[12]+"\n");T.insert('14.0',yc[13]+"\n");T.insert('15.0',yc[14]+"\n\n\n\n\n")
                replace_line("users.txt",0,yc[0]+"\n")
                replace_line("users.txt",1,yc[1]+"\n")
                replace_line("users.txt",2,yc[2]+"\n")
                replace_line("users.txt",3,yc[3]+"\n")
            except: print("wtf")
        
        
        sm.current = "Second"
        class SecondWindow(Screen):
            c1b = open("users.txt", "r").readlines()[0]; c1a=c1b.strip(); yc1=str(c1a)
            c1b = open("users.txt", "r").readlines()[1]; c1a=c1b.strip(); yc2=str(c1a)
            c1b = open("users.txt", "r").readlines()[2]; c1a=c1b.strip(); yc3=str(c1a)
            c1b = open("users.txt", "r").readlines()[3]; c1a=c1b.strip(); yc4=str(c1a)
            IPLabel = yc1
            IPLabel2 =yc2
            IPLabel3 =yc3
            IPLabel4 =yc4
            def aanwezig(self):
                sql = f"UPDATE {groep2} SET week{self.weeknumber} = 0 WHERE naam = '{self.email.text}'"
                mycursor.execute(sql)
                try: mydb.commit()
                except: print("Updaten is niet gelukt")
                print("Aanwezig")
                sm.current = "main"
            def afwezig(self):
                sql = f"UPDATE {groep2} SET week{self.weeknumber} = 1 WHERE naam = '{self.email.text}'"
                mycursor.execute(sql)
                try: mydb.commit()
                except: print("Updaten is niet gelukt")
                print("Afwezig")
                sm.current = "main"

class SecondWindow(Screen):
    c1b = open("users.txt", "r").readlines()[0]; c1a=c1b.strip(); yc1=str(c1a)
    c1b = open("users.txt", "r").readlines()[1]; c1a=c1b.strip(); yc2=str(c1a)
    c1b = open("users.txt", "r").readlines()[2]; c1a=c1b.strip(); yc3=str(c1a)
    c1b = open("users.txt", "r").readlines()[3]; c1a=c1b.strip(); yc4=str(c1a)
    IPLabel = yc1
    IPLabel2 =yc2
    IPLabel3 =yc3
    IPLabel4 =yc4
    
    
    def aanwezig(self):
        self.weeknumber2 = value2[:-1]
        print("self.weeknumber2 = ", self.weeknumber2)
        
        self.weeknumber = self.weeknumber2[+32:]
        sql = f"UPDATE {groep2} SET week{self.weeknumber} = 0 WHERE naam = '{loginname}'"
        mycursor.execute(sql)
        try: mydb.commit()
        except: pass
        sm.current = "main"
    def afwezig(self):
        self.weeknumber2 = value2[:-1]
        print("self.weeknumber2 = ", self.weeknumber2)
        
        self.weeknumber = self.weeknumber2[+32:]
        sql = f"UPDATE {groep2} SET week{self.weeknumber} = 1 WHERE naam = '{loginname}'"
        mycursor.execute(sql)
        try: mydb.commit()
        except: pass
        sm.current = "main"
          
class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
#db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),SecondWindow(name="Second")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
