from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
import mysql.connector as sql
import smtplib
import pickle
X=Tk()
X.geometry('2000x1000+5+5')
z=0    
name=no=email=PINCODE=district=PASS=GMAP=locality=address=""
def CREATE():
    def error(error):       
        p=Tk()
        p.configure(background='light yellow')
        p.geometry('150x75+750+600')
        Label(p,text=error,fg="red",bg='light yellow').pack()
        p.mainloop()
    def image(X,x,y):
        image=Image.open("LOGO.png")
        resize=image.resize((x,y ))
        img=ImageTk.PhotoImage(resize)
        L1=ttk.Label(X,image=img)
        L1.image=img
        L1.pack()
#----------------------------------------------------------------------------------
    def entry(X,p,c,x,y=5):
        _var=StringVar()
        user=Label(X,text=p,bg=c).pack(ipadx=x,ipady=y)
        userentry=Entry(X,textvariable=_var).pack(ipadx=110,ipady=3)
        return _var     
#------------------------------------------------------------------------------
    def sb(X,t,c):
         s=Button(X,text=t,command=c,fg="blue",bg="light green").pack(ipadx=110,ipady=7) 
#------------------------------------------------------------------------------
    def log():
        def cre():
            global X
            p.destroy()
            X=Tk()
            create()
        def loginverify():
            no=no_var.get()
            pw=password_var.get()
            con=sql.connect(host="localhost",user="root",passwd="--",database="user-details")
            if con.is_connected():
                print("p")
            cursor=con.cursor()
            cursor.execute("SELECT * FROM `user-details`.`customer_details`;")
            data=("A")
            while data!=None:
                g=k=0
                data=cursor.fetchone()         
                if data==None:                  
                    error("ACCOUNT DOESN'T EXIST")
                    break                    
                elif data!=None:
                    if (data[2]==no or data[3]==no)and data[-1]==pw:
                        break
                    else:                      
                        error("wrong login details")
                        break
                        
        X.destroy()
        p=Tk()
        p.geometry('500x350+750+400')
        image(p,500,100)
        no_var=entry(p,"ENTER PHONE OR GMAIL R EGISTERED","yellow",130)
        password_var=entry(p,"ENTER YOUR PASSWORD","RED",150)
        sb(p,"LOGIN",loginverify)
        sb(p,"DON'T HAVE A ACCOUNT CREATE HERE",cre)
        p.mainloop()
    def create():
        otp=str(random.randint(1000,10000))
        def submit():
            global n
            name=name_var.get()
            no=str(no_var.get())
            email=email_var.get()
            address=add_var.get()
            district=DISTRICT_VAR.get()
            PINCODE=pin_VAR.get()
            GMAP=GMAP_VAR.get()
            PASS=PASS_VAR.get()
            locality=loc_var.get()
            OTP=OTP_VAR.get()
            con=sql.connect(host="localhost",user="root",passwd="kamalesh***@@@",database="user-details")
            if con.is_connected():
                print("p")
            cursor=con.cursor()
            cursor.execute("SELECT * FROM `user-details`.`customer_details`;")
            data=cursor.fetchall()
            def checkno():
                c=a=p=n=g=0
                for i in no:
                    a+=1
                    if i.isdigit():
                        c+=1
                if c==10 and a==10:
                    if data==[]:
                        n=1
                    elif data!=[]:
                        for i in data:
                            print
                            if no in i:
                                error("NUMBER ALREADY EXIST")
                                n=0
                                break
                            else:
                                n=1
                else:
                    error("ENTER VALID NUMBER")   
                return n                 
            def checkemail():
                n=0
                if data==[]:
                    n=1
                elif data!=[]:
                    for i in data:
                        if email.lower() in i or email.upper()in i:
                            error("EMAIL ALREADY EXIST")
                            break
                        else:
                            n=1
                return n
            def password():
                n=0
                for i in PASS:
                    n+=1
                if n>=10:
                    n=1
                return n
            def check():
                i=0
                for x in(name,address,PINCODE,GMAP,locality):
                    if x=="":
                        error("ENTER VALID DETAILS")
                        i+=1
                return i
            check()
            n=checkno()
            e=checkemail()
            p=password()
            print(n,e,check())
            if e==1 and n==1 and check()==0:
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login("<@gmail.com","pwd")
                message="YOUR OTP IS:"+str(otp)
                print(message)
                s.sendmail("email",email,message)
                s.quit()
                if otp==OTP:
                    print("l")
                    st="INSERT INTO `user-details`.`customer_details`(`namecustomer`,`nocustomer`,`emailcustomer`,`addresscustomer`,`districtcustomer`,`localitycustomer`,`pincodecustomer`,`gmapcustomer`,`passwdcustomer`) VALUE('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,no,email,address,district,locality,PINCODE,GMAP,PASS);
                    cursor.execute(st)
                    con.commit()
                    details={'name':name,'no':no,'email':email,'address':address,'locality':locality,'district':district,'pincode':PINCODE,'GMAP':GMAP,"ps":PASS}
                    global z
                elif z==1:
                    error("wrong otp")
                else:                   
                    z=1
        image(X,2000,200)
        name_var=entry(X,"ENTER FULL NAME","VIOLET",120)
        no_var=entry(X,"ENTER PHONE NUMBER","PINK",108)
        email_var=entry(X,"ENTER GMAIL ID","LIGHT BLUE",126)
        add_var=entry(X,"ENTER ADDRESS","ORANGE",126)
        loc_var=entry(X,"ENTER YOUR LOCALITY","LIGHT YELLOW",107)
        DISTRICT_VAR=entry(X,"ENTER YOUR DISTRICT","LIGHT GREEN",110)
        pin_VAR=entry(X,"ENTER PIN CODE","PURPLE",125)
        GMAP_VAR=entry(X,"ENTER YOUR GMAP LOCATION LINK","RED",75)
        PASS_VAR=entry(X,"CREATE PASSWORD","CYAN",115)
        sb(X,"SEND OTP",submit)
        LINESPACING=Label(X,text="\n").pack(ipadx=120,ipady=2)
        OTP_VAR=E=entry(X,"ENTER OTP END TO YOUR GMAIL ID, IF OTP NOT RECEIVED CHECK YOUR EMAIL ADDRESS","CYAN",50)
        H=Button(X,text="VERIFY OTP AND CREATE ACCOUNT",command=submit,fg="blue",bg="light green").pack(ipadx=110,ipady=9)
        H=Button(X,text="HAVE A ACCOUNT LOGIN HERE",command=log,fg="blue",bg="light green").pack(ipadx=110,ipady=9)  
    create()
    X.mainloop()
def homepage():
    global X
    X.destroy()
    X=Tk()
    X.geometry('2000x1000+5+5')
    D=Label(X,text=" ",bg="yellow").pack(side=top)
CREATE()
