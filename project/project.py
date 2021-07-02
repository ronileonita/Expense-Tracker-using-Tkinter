from tkinter import *
from PIL import ImageTk,Image 

def Signuppage():
	global w
	w.destroy()
	from signup import Signup
	Signup()

def Loginbutton():
	w.destroy()
	from login import Login
	Login()
def Mainpage():	
	global w	
	w=Tk()	
	w.config(bg="#ffffff")
	load = Image.open("images/home.png")
	render = ImageTk.PhotoImage(load)
	img = Label(w, image=render)
	img.place(x=0, y=0)

	lbl=Label(img,text="EXPENSE TRACKER",font=("Georgia",30,"bold"),fg="black", bg="#33ccff")
	lbl.place(x=(render.width()/2)-250,y=10)

	sign = Image.open("images/signupIcon.jpg")
	sign = ImageTk.PhotoImage(sign)
	signup=Button(w,text="SIGN IN",image=sign,border=0,command=Signuppage)
	signup.place(x=render.width()+200,y=80)

	log = Image.open("images/loginIcon.jpg")
	log = ImageTk.PhotoImage(log)
	login=Button(w,text="LOG IN",image=log, border=0,command=Loginbutton)
	login.place(x=render.width()+200,y=render.height()+10)

	lbl4=Label(w,text="Expense tracker is complete app to track your all the expenses bared by your pocket\n or bared by you & manage your personal finance. So that you can trace where your money\n goes as well as from where money comes in, you can limit & plan accordingly.\n\n A feature rich tracking application with numerous powerful tools like Income/Expense, Bills,\n Accounts, Reports etc. Not only that, app has all the information yet not un-secure\n as it does not ask to save any sensitive data for its operations.\n\nAlso features like Income/Expense,keep tracking of your incoming & outgoing flows, Bills\n maintain your recurring expenses & keep reminding you as your helping hand.\n\n Out of these features reports is a mind blowing Artificial intelligence based feature\n that analyzes based on your data and gives graphical results of your income & expenses.\n Over all a powerful personal finance tool that keeps on improving your productivity, \nsaves a time & helps you to save your money.",bg="#449ff3",fg="#ffffff",font=("Lucida Sans Unicode",12))
	lbl4.place(x=0,y=render.height()-8,width=render.width()+2,height=300)
	w.state('zoomed')
	w.mainloop()

