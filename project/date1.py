from tkinter import *
import calendar
from datetime import *
from PIL import Image,ImageTk
from tkinter import messagebox
from login import *
def setdate(Uid):
	def value():
		flag=0
		feb=0 
		m = mon.get()
		for i in range(len(months)):
			if m == months[i]:
				pos = i
				if i==11:
					end_m = months[0]
					end_y = int(now.strftime("%Y"))+1
				else:	
					end_m = months[i+1]
		for i in range(len(months)):
			for j in range(len(monx)):
				if pos==j:
					if monx[j]==0 and int(dt.get())==31:
						flag = 1
					elif monx[j]== -1:
						if int(y.get())%4==0 and int(dt.get())>29:
							feb=1
						elif int(dt.get())>28:
							feb=2
		if flag==1:
			messagebox.showinfo("Error", m + " has only 30 days!")
		elif feb==1:
			messagebox.showinfo("Error", m + " has only 29 days!")
		elif feb==2:
			messagebox.showinfo("Error", m + " has only 28 days!")
		elif len(ent.get())==0:
			messagebox.showinfo("Error", "Set maximum limit")		
		start_date = y.get()+"-"+mon.get()+"-"+dt.get()
		end_d = int(dt.get())-1
		end_date = y.get()+"-"+end_m+"-"+str(end_d)
		sd = datetime.strptime(start_date, '%Y-%B-%d')
		ed = datetime.strptime(end_date, '%Y-%B-%d')

		import pymysql as mysqli
		hostname="localhost"
		dbuser="root"
		dbpass=""
		dbname="expense"
		conn=mysqli.connect(hostname,dbuser,dbpass,dbname)
		cursor=conn.cursor()
		query="insert into dateinfo(START_DATE,END_DATE,MAX_EXP,UID)values('"+str(sd)+"','"+str(ed)+"','"+ent.get()+"','"+str(Uid)+"')"
		res=cursor.execute(query)
		conn.commit()
		if res==1:
			print("Account Created")
		else:
			print("Can't create account")	
		conn.close()
		master.destroy()

	global master
	master = Toplevel(win)	
	master.state('zoomed')
	date=[]
	for i in range(1,32):
		date.append(i)
	months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
	monx = [1,-1,1,0,1,0,1,1,0,1,0,1]
	year = [2019,2020,2021,2022]
	d1=["15 days","1 Month","2 Month"]
	now = datetime.now()
	master.config(bg='#ffffff')
	f = ('Georgia' , 40 , 'italic')
	f1 = ('Georgia' , 20 , 'bold')	
	load = ImageTk.PhotoImage(Image.open("images/calendar.jpg"))
	img = Label(master, image=load)
	img.place(x=200,y=200)

	lb = Label(master, text="Set Date", font=f, fg='#449ff3',bg='#ffffff')
	lb.place(x=180,y=100)

	lb1 = Label(master, text="Start Date", font=f1, fg='#449ff3',bg='#ffffff')
	lb1.place(x=450,y=250)

	mon = StringVar(master)
	mon.set(now.strftime("%B")) # default value
	m = OptionMenu(master, mon, *months)
	m.config(compound='right')
	m.place(x=450,y=300)

	dt = StringVar(master)
	dt.set(now.strftime("%d"))
	d = OptionMenu(master, dt, *date)
	d.place(x=550,y=300)

	y = StringVar(master)
	y.set(now.strftime("%Y"))
	y1 = OptionMenu(master, y, *year)
	y1.place(x=620,y=300)

	lb1 = Label(master, text="Duration", font=f1, fg='#449ff3',bg='#ffffff')
	lb1.place(x=450,y=350)

	duration = StringVar(master)
	duration.set(d1[1])
	d1 = OptionMenu(master, duration, *d1)
	d1.place(x=460,y=400)

	lb2 = Label(master, text="Set Maximum limit\n of expense", font=('Georgia' , 35 , 'italic'), fg='#449ff3',bg='#ffffff')
	lb2.place(x=750,y=100)

	load1 = ImageTk.PhotoImage(Image.open("images/exp.jpg"))
	img1 = Label(master, image=load1)
	img1.place(x=770,y=250)

	e = Label(master, text="Rs.",font=f1)
	e.place(x=800,y=450)
	ent = Entry(master,font=f1,border=3, width=10)
	ent.place(x=850,y=450)

	btn = Button(master, text="DONE" , font=f1 , fg="#ffffff", border=3,bg="#449ff3", command=value)
	btn.place(x=600,y=530)

	
	mainloop()