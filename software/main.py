import tkinter as tk
import tkinter.font as tkf
import datetime as dt
from datetime import datetime as dts
from threading import Thread
import os
from time import *
root = tk.Tk()
root.geometry("640x300")
root.title("Create File")
root.configure(bg="blue")
class adj:
	def __init__(self):
		self.stopper = False
		self.h  = 0
		self.m = 0
		self.s  = 0
add = adj()

class timer(Thread):
	def run(self):
		while not add.stopper:
			tmr = tk.Label(text = "Time -   {}:{}:{}".format(add.h,add.m,add.s))
			tmr.configure(bg="blue",foreground="white")
			tmr.pack(side = tk.LEFT)
			cnvs.create_window(440,20,window = tmr)
			sleep(1)
			add.s+=1
			if add.s == 60:
				add.s = 0
				add.m+=1
			if add.m == 60:
				add.m = 0
				add.h += 1
			if add.stopper:
					add.s = 0
					add.m = 0
					add.h = 0
					tmr = tk.Label(text = "Time -   {}:{}:{}".format(add.h,add.m,add.s))
					tmr.configure(bg="blue",foreground="white")
					tmr.pack(side = tk.LEFT)
					cnvs.create_window(440,20,window = tmr)
		return
obj1 = timer(daemon = True)
#FILE CREATE CODE START
# Label
fn1 = tkf.Font(size=20)
title = tk.Label(root,text="Create File")
title.configure(bg="blue",foreground="white",font=fn1)
title.pack()
#canvas One
cnvs = tk.Canvas(root,width = 540,height = 150)
cnvs.pack(side=tk.LEFT,pady=30)
cnvs.configure(bg="blue")
#canvas Two
cnvs2 = tk.Canvas(root,width = 100,height = 150)
cnvs2.pack(side=tk.RIGHT,pady=30)
cnvs2.configure(bg="blue")

# Title Label one 
fn1 = tkf.Font(size=10)
title_label = tk.Label(root,text="Create File")
title_label.configure(bg="blue",foreground="white",font=fn1)
title_label.pack()
cnvs.create_window(270,20,window = title_label)
# Input Box
entry = tk.Entry(root,width=50)
fn2 = tkf.Font(family="Lucida Console")
entry.configure(bg="white",font=fn2)
entry.pack(side=tk.LEFT,padx=10,pady=10)
cnvs.create_window(270,55,window = entry)
# Class to kil thread
class killer(Thread):
	def run(self):
		if obj1.is_alive() and not add.stopper :
			add.stopper = True
			obj1.join()
			obj1._stop()
			return
t2 = killer(daemon = True)
def ee():
	if(not t2.is_alive) :
		t2.start()
	if t2.is_alive() :
		t2.join()
		t2._stop()	
	add.s = 0
	add.m = 0
	add.h = 0
	tmr = tk.Label(text = "Time -   {}:{}:{}".format(add.h,add.m,add.s))
	tmr.configure(bg="blue",foreground="white")
	tmr.pack(side = tk.LEFT)
	cnvs.create_window(440,20,window = tmr)
def file_creator():
	ee()
	name = entry.get()
	s = "	* Author :- Tanay Kulkarni\n"
	s +=  "	* Date   :- "
	obj = dts.now()
	s+= "{}-{}-{}".format(obj.day,obj.month,obj.year)
	s+="\n"
	s+= "	* Time   :- "
	s+= str(dts.now().time())
	s+="\n"
	s +=  "	* Name   :- "
	s+=name
	s+='\n'
	if '.cpp' in name:
		s = "/*\n"+s+"*/\n"
		template = open("ctemplate.cpp",'r')
		s+= template.read()
		f = open(name,'w')
		f.write(s)
		f.close()
	elif '.java' in name:
		
		s = "/*\n"+s+"*/\n"
		s += "import java.util.*;\nimport java.io.*;\npublic class "
		for let in name:
			if let == '.':
				break
			s += let
		s += '{\n'
		template = open("jtemp.java",'r')
		s+= template.read()
		f = open(name,'w')
		f.write(s)
		f.close()
	else:
		s = "'''\n"+s+"'''\n"
		template = open("pytemp.py",'r')
		s+= template.read()
		f = open(name,'w')
		f.write(s)
		f.close()
	if not obj1.is_alive() :
		add.stopper = False
		obj1.start()
#	os.system("subl {}".format(name))
# Button
bf = tkf.Font(size=10)
btn = tk.Button(text="CREATE",width=9,command=file_creator)
btn.configure(font=bf,bg="yellow",foreground="black")
btn.pack(side=tk.LEFT,padx=10,pady = 20)
cnvs2.create_window(50,55,window = btn)

#FILE CREATE CODE END
# CMD CODE START
# Title Label two
fn1 = tkf.Font(size=10)
title_label_2 = tk.Label(root,text="Command Prompt")
title_label_2.configure(bg="blue",foreground="white",font=fn1)
title_label_2.pack()
cnvs.create_window(270,90,window = title_label_2)
#input box
entry2 = tk.Entry(root,width=50)
fn2 = tkf.Font(family="Lucida Console")
entry2.configure(bg="white",font=fn2)
entry2.pack(side=tk.RIGHT,padx=10,pady=10)
cnvs.create_window(270,120,window = entry2)
def runner():
	cm = entry2.get()
	os.system(cm)
#Button
btn2 = tk.Button(text="RUNCMD",width=9,command=runner)
btn2.configure(font=bf,bg="yellow",foreground="black")
btn2.pack(side=tk.RIGHT,padx=10,pady = 20)
cnvs2.create_window(50,120,window = btn2)
# CMD CODE END
# Reset Button
bf = tkf.Font(size=10)
btn3 = tk.Button(text="RESET",width=9,command=ee())
btn3.configure(font=bf,bg="yellow",foreground="black")
btn3.pack(side=tk.LEFT,padx=10,pady = 0)
cnvs2.create_window(50,20,window = btn3)
#global stopper
ee()
root.mainloop()	
'''
s+='void debug(string j){')
s+='\n'
s+='cout<<"| Value : "<<j<<" |\n";')
s+='\n'
s+='}'
s+='\n'
s+='void debug(int j){'
s+='\n'
s+='cout<<"| Value : "<<j<<" |\n";')
s+='\n'
s+='}'
s+='\n'
s+='void debug(int i,string j){'
s+='\n'
s+='cout<<"Iteration "<<i<<": "<<j<<"\n";'
s+='\n'
s+='}'
s+='\n'
s+='void debug(int i,int j){'
s+='\n'
s+='cout<<"Iteration "<<i<<": "<<j<<"\n";'
s+='\n'
s+='}'
s+='\n'
'''

