from tkinter import *
from login import *
def UserInfo(u,p):	
	global topl
	topl=Toplevel(win)
	topl.config(bg="#3EC39F")
	topl.geometry("%dx%d+%d+%d" % (1500,750,0,0))
			
	btn=Button(topl,text="back",font=(10),command=topl.destroy)
	btn.place(x=10,y=10)
			
	lbl=Label(topl,text="MY ACCOUNT",font=("Georgia",30,"bold"),bg="#3EC39F")
	lbl.place(x=200,y=10,width=500,height=50)
	lbl=Label(topl,text="NAME :",font=(10),bg="#3EC39F",anchor=W)
	lbl.place(x=100,y=200,width=200,height=50)
	
	lbl8=Label(topl,font=(10),anchor=W)
	lbl8.place(x=300,y=200,width=300,height=50)
	lbl=Label(topl,text="USERNAME :",font=(10),bg="#3EC39F",anchor=W)
	lbl.place(x=100,y=300,width=200,height=50)
		
	lbl9=Label(topl,font=(10),anchor=W)
	lbl9.place(x=300,y=300,width=300,height=50)
	lbl=Label(topl,text="EMAIL :",font=(10),bg="#3EC39F",anchor=W)
	lbl.place(x=100,y=400,width=200,height=50)
		
	lbl10=Label(topl,font=(10),anchor=W)
	lbl10.place(x=300,y=400,width=300,height=50)
	lbl=Label(topl,text="PHONE NUMBER :",font=(10),bg="#3EC39F",anchor=W)
	lbl.place(x=100,y=500,width=200,height=50)
		
	lbl11=Label(topl,font=(10),anchor=W)
	lbl11.place(x=300,y=500,width=300,height=50)
	lbl=Label(topl,text="YOUR PASSWORD :",font=(10),bg="#3EC39F",anchor=W)
	lbl.place(x=100,y=600,width=200,height=50)
		
	lbl12=Label(topl,font=(10),anchor=W)
	lbl12.place(x=300,y=600,width=300,height=50)
	import pymysql as mysqli
	hostname="localhost"
	dbuser="root"
	dbpass=""
	dbname="expense"
	conn=mysqli.connect(hostname,dbuser,dbpass,dbname)
	cursor=conn.cursor()
	query="select * from userinfo"
	cursor.execute(query)
	row=cursor.fetchall()
	for x in row:
		if x[2]==u and x[5]==p:
			name=x[1]
			usern=x[2]
			email=x[3]
			phone=x[4]
			passw=x[5]
			lbl8.config(text=name)
			lbl9.config(text=usern)
			lbl10.config(text=email)
			lbl11.config(text=phone)
			lbl12.config(text=passw)
	conn.close()