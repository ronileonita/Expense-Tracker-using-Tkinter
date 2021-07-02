from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from config import *
import smtplib

def Login():
	def Todayexpense():
		from today import Todaysexpense
		Todaysexpense()
		
	def Userinfo():
		from UserInformation import UserInfo
		UserInfo(u,p)

	def SetDate():
		from date1 import setdate
		setdate(Uid)	
		
	def Otherfun():
		win.destroy()
		from login import Login
		Login()
	def App(uid,user):
		global win
		toppw.destroy()
		win=Tk()
		win.config(bg="#ffffff")
		win.state('zoomed')

		print(uid)
		btn=Button(win,text="SIGN OUT",command=Otherfun)
		btn.place(x=1000,y=10,width=90,height=40)

		lbl7=Label(win,text="WELCOME "+ user ,font=("Georgia",30,"bold"),bg="#ffffff")
		lbl7.place(x=400,y=10) 

		canvas = Canvas(win, width = 200, height = 200)  
		canvas.place(x=250,y=150)  
		ima = ImageTk.PhotoImage(Image.open("images/user.jpg"))  
		canvas.create_image(0,0, anchor=NW, image=ima)
		btn=Button(win,text="View your info",bg='#ffffff',command=Userinfo,font=(10))
		btn.place(x=250,y=360,width=200,height=50)

		canvas = Canvas(win, width = 200, height = 200)  
		canvas.place(x=600,y=150)  
		imag = ImageTk.PhotoImage(Image.open("images/date.jpg"))  
		canvas.create_image(0,0, anchor=NW, image=imag)
		btn=Button(win,text="Set date",bg='#ffffff',command=SetDate,font=(10))
		btn.place(x=600,y=360,width=200,height=50)

		canvas = Canvas(win, width = 200, height = 200)
		canvas.place(x=950,y=150)  
		image = ImageTk.PhotoImage(Image.open("images/today.jpg"))  
		canvas.create_image(0,0, anchor=NW, image=image)
		btn=Button(win,text="Today's expense",command=Todayexpense,bg='#ffffff',font=(10))
		btn.place(x=950,y=360,width=200,height=50)

		canvas = Canvas(win, width = 200, height = 200) 
		canvas.place(x=250,y=450)  
		imagee = ImageTk.PhotoImage(Image.open("images/list.jpg"))  
		canvas.create_image(0,0, anchor=NW, image=imagee)
		btn=Button(win,text="View the stored items",bg='#ffffff',font=(10))
		btn.place(x=250,y=660,width=200,height=50)

		canvas = Canvas(win, width = 200, height = 200)  
		canvas.place(x=600,y=450)  
		imageee = ImageTk.PhotoImage(Image.open("images/view.jpg"))  
		canvas.create_image(0,0, anchor=NW, image=imageee)
		btn=Button(win,text="View ",bg='#ffffff',font=(10))
		btn.place(x=600,y=660,width=200,height=50)

		canvas = Canvas(win, width = 200, height = 200)  
		canvas.place(x=950,y=450)  
		image1 = ImageTk.PhotoImage(Image.open("images/graph.jpg"))  
		canvas.create_image(0,0, anchor=NW, image=image1)
		btn=Button(win,text="View your graph",bg='#ffffff',font=(10))
		btn.place(x=950,y=660,width=200,height=50)
		win.mainloop() 

	def call_forgot():
		def forgot():
			success=0
			text1=e.get()
			import pymysql as mysqli
			hostname="localhost"
			dbuser="root"
			dbpass=""
			dbname="expense"
			conn=mysqli.connect(hostname,dbuser,dbpass,dbname)
			cursor=conn.cursor()
			query="select * from userinfo"
			cursor.execute(query)
			cursor.close()
			row=cursor.fetchall()
			for x in row:
				if x[3]==text1:
					smtp=smtplib.SMTP("smtp.gmail.com",587)
					smtp.ehlo()
					smtp.starttls()
					smtp.ehlo()
					smtp.login(username,password)
					subject="Your Password"
					body="You Password is '"+x[5]+"'"
					msg='subject:'+subject+'\n\n'+body
					smtp.sendmail(username,x[3],msg)
					success=1
					break
			conn.close()
			if success==0:
				messagebox.showinfo("Error","Email is not registerd")
			else:
				messagebox.showinfo("Success","Email is sent")

		top = Toplevel(toppw)
		top.config(bg="#ffffff")
		top.geometry("%dx%d+%d+%d" % (500, 200,380 ,100))
		lb = Label(top,text="Enter your registerd email id", bg='#ffffff',font=f1)
		lb.place(x=100,y=50)
		em = Label(top,text="Email" , bg="white", font=f1)
		em.place(x=100,y=100)
		e = Entry(top, font=(10), border=3)
		e.place(x=200,y=100, height=30)

		btn = Button(top, text="Done", bg="#449ff3", fg="white", command=forgot)
		btn.place(x=250,y=150,height=35,width=100)

		top.mainloop()

	def call_reset(user):
		def Reset():
			success=0
			text=oldu.get()
			text1=oldInp.get()
			text2=newInp.get()
			text3=conInp.get()
			if text2!=text3:
				messagebox.showinfo("Error","Passowrd did not match")
			else:
				import pymysql as mysqli
				hostname="localhost"
				dbuser="root"
				dbpass=""
				dbname="expense"
				conn=mysqli.connect(hostname,dbuser,dbpass,dbname)
				cursor=conn.cursor()
				query="select * from userinfo"
				cursor.execute(query)
				cursor.close()
				row=cursor.fetchall()
				for x in row:
					if x[2]==text and x[5]==text1:
						cur=conn.cursor()
						q = "update userinfo set PASSWORD ='"+text2+" 'where USERNAME='"+text+"'"
						cur.execute(q)
						conn.commit()
						cur.close()
						conn.close()
						success=1
				if success==0:
					messagebox.showinfo("Error","Username or password is wrong")
				else:
					messagebox.showinfo("Error","Password Updated")
						
		top = Toplevel(toppw)
		top.config(bg="#ffffff")
		top.geometry("%dx%d+%d+%d" % (600, 500,400 ,80))
		u1 = Label(top,text="Username" , bg="white", font=f1)
		u1.place(x=100,y=100)
		oldu = Entry(top, font=(10))
		oldu.place(x=320,y=100, height=30)

		old = Label(top,text="Old Password" , bg="white", font=f1)
		old.place(x=100,y=150)
		oldInp = Entry(top, font=(10))
		oldInp.place(x=320,y=150, height=30)
		new = Label(top,text="New Password" , bg="white", font=f1)
		new.place(x=100,y=200)
		newInp = Entry(top, font=(10))
		newInp.place(x=320,y=200, height=30)

		confirm = Label(top,text="Re-enter Password" , bg="white", font=f1)
		confirm.place(x=100,y=250)
		conInp = Entry(top,font=(10))
		conInp.place(x=320,y=250, height=30)

		btn = Button(top, text="Done", bg="#449ff3", fg="white", command=Reset)
		btn.place(x=360,y=300,height=35,width=100)

		top.mainloop()
	def Anotherfun(uid,user):
		global Uid
		global User
		Uid = uid
		User = user
		App(uid,user)
	def Twofun():
		toppw.destroy()
		from project import Mainpage
		Mainpage()
	
	def Check():
		success=0
		global u,p
		u = userInp.get()
		p = pswInp.get()
		if len(u)==0 or len(p)==0:
			messagebox.showinfo("Error","Enter username and password ")
		else:
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
					Anotherfun(x[0],x[1])
					success=1
			if success==0:
				messagebox.showinfo("Error","Username or password is wrong")
				#conn.close()				
	toppw = Tk()
	toppw.config(bg="#ffffff")
	load = Image.open("images/login.png")
	render = ImageTk.PhotoImage(load)
	img = Label(toppw, image=render)
	img.image = render
	img.place(x=400, y=50)
		
	f = ('Georgia' , 40 , 'bold')
	f1 = ('Georgia' , 15 , 'bold')
	lb = Label(img, text="LOGIN" , bg="white" , font=f)
	lb.place(x = (render.width()/2)-90 , y = render.height()/3)

	user = Label(img,text="Username" , bg="white", font=f1)
	user.place(x=(render.width()/2)-135,y=render.height()-250)
	userInp = Entry()
	userInp.place(x=render.width()+30,y=render.height()-200, height=30)

	psw = Label(img,text="Password" , bg="white", font=f1)
	psw.place(x=(render.width()/2)-135,y=render.height()-200)
	pswInp = Entry()
	pswInp.place(x=render.width()+30,y=render.height()-150, height=30)


	link = Label(img,text="Forgot Password", cursor = "hand2",bg="white", fg="blue")
	link.place(x=render.width()-300,y=render.height()-150)
	link.bind("<Button-1>", lambda e: call_forgot())

	link = Label(img,text="Reset Password", cursor = "hand2",bg="white", fg="blue")
	link.place(x=render.width()-400,y=render.height()-150)
	link.bind("<Button-1>", lambda e: call_reset(userInp))

	btn = Button(img, text="Submit", font=f1 , bg="#449ff3" , fg = "white" , command=Check)
	btn.place(x=render.width()-370,y=render.height()-100)

	toppw.state('zoomed')
	back = Image.open("images/back.jpg")
	back = ImageTk.PhotoImage(back)
	btn=Button(toppw,text="BACK",image=back,border=0,command=Twofun)
	btn.place(x=0,y=0)
	toppw.mainloop()
		