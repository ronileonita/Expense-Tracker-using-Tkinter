from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from config import *
import smtplib
from login import *

def Todaysexpense():

		global topp
		
		topp = Toplevel(win)
		topp.config(bg="#ffffff")
		topp.geometry("%dx%d+%d+%d" % (1500,750,0,0))
		l=Label(topp,text="Enter your today's expense",fg="black",font=("Georgia",30,"bold"))
		l.place(x=300,y=10,width=600,height=50)
		btn=Button(topp,text="BACK",font=(10),command=topp.destroy)
		btn.place(x=10,y=10)


		load = Image.open("images/edu.png")
		render = ImageTk.PhotoImage(load)
		img = Label(topp, image=render)
		img.image = render
		img.place(x=100, y=150,width=200,height=200)
		btn=Button(topp,text="Education",bg='#ffffff',font=(10))
		btn.place(x=100,y=360,width=200,height=50)

		load = Image.open("images/travell.png")
		render = ImageTk.PhotoImage(load)
		img = Label(topp, image=render)
		img.image = render
		img.place(x=350, y=150,width=200,height=200)
		btn=Button(topp,text="Travel",bg='#ffffff',font=(10))
		btn.place(x=350,y=360,width=200,height=50)

		load = Image.open("images/grocery.png")
		render = ImageTk.PhotoImage(load)
		img = Label(topp, image=render)
		img.image = render
		img.place(x=600, y=150,width=200,height=200)
		btn=Button(topp,text="Grocery",bg='#ffffff',font=(10))
		btn.place(x=600,y=360,width=200,height=50)

		load = Image.open("images/bills.png")
		render = ImageTk.PhotoImage(load)
		img = Label(topp, image=render)
		img.image = render
		img.place(x=850, y=150,width=200,height=200)
		btn=Button(topp,text="Bills",bg='#ffffff',font=(10))
		btn.place(x=850,y=360,width=200,height=50)

		load = Image.open("images/electro.png")
		render = ImageTk.PhotoImage(load)
		img = Label(topp, image=render)
		img.image = render
		img.place(x=1100, y=150,width=200,height=200)
		btn=Button(topp,text="Electronics",bg='#ffffff',font=(10))
		btn.place(x=1100,y=360,width=200,height=50)

		load = Image.open("images/enter.png")
		render = ImageTk.PhotoImage(load)
		img = Label(topp, image=render)
		img.image = render
		img.place(x=100, y=450,width=200,height=200)
		btn=Button(topp,text="Entertainment",bg='#ffffff',font=(10))
		btn.place(x=100,y=660,width=200,height=50)

		load = Image.open("images/clothes.png")
		render = ImageTk.PhotoImage(load)
		img = Label(topp, image=render)
		img.image = render
		img.place(x=350, y=450,width=200,height=200)
		btn=Button(topp,text="Clothes",bg='#ffffff',font=(10))
		btn.place(x=350,y=660,width=200,height=50)

		load = Image.open("images/health.png")
		render = ImageTk.PhotoImage(load)
		img = Label(topp, image=render)
		img.image = render
		img.place(x=600, y=450,width=200,height=200)
		btn=Button(topp,text="Health",bg='#ffffff',font=(10))
		btn.place(x=600,y=660,width=200,height=50)

		load = Image.open("images/saving.png")
		render = ImageTk.PhotoImage(load)
		img = Label(topp, image=render)
		img.image = render
		img.place(x=850, y=450,width=200,height=200)
		btn=Button(topp,text="Savings",bg='#ffffff',font=(10))
		btn.place(x=850,y=660,width=200,height=50)

		load = Image.open("images/other.png")
		render = ImageTk.PhotoImage(load)
		img = Label(topp, image=render)
		img.image = render
		img.place(x=1100, y=450,width=200,height=200)
		btn=Button(topp,text="Other",bg='#ffffff',font=(10))
		btn.place(x=1100,y=660,width=200,height=50)

