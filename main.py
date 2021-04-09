import tkinter as tk
import tkinter.font as tkf
import datetime as dt
from datetime import datetime as dts
from threading import Thread
import os
from time import *
root = tk.Tk()
root.geometry("640x300")
root.title("File Formatter")
root.configure(bg="blue")
stopper = False
class timer(Thread):
	def run(self):
		h = 0
		m = 0
		s = 0
		while(True):
			tmr = tk.Label(text = "Time -   {}:{}:{}".format(h,m,s))
			tmr.configure(bg="blue",foreground="white")
			tmr.pack(side = tk.LEFT)
			cnvs.create_window(460,20,window = tmr)
			sleep(1)
			s+=1
			if s == 60:
				s = 0
				m+=1
			if m == 60:
				m = 0
				h += 1
			if stopper == False:
				s = 0
				m = 0
				h = 0
				return
obj1 = timer()
#FILE CREATE CODE START
# Label
fn1 = tkf.Font(size=20)
title = tk.Label(root,text="File Formatter")
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

#'''
def file_creator():
	global stopper
	stopper = True
	name = entry.get()
	s = "/*\n"
	s += "	Author :- Tanay Kulkarni\n"
	s +=  "	Date   :- "
	obj = dts.now()
	s+= "{}-{}-{}".format(obj.day,obj.month,obj.year)
	s+="\n"
	s+= "	Time   :- "
	s+= str(dts.now().time())
	s+="\n"
	s +=  "	Name   :- "
	s+=name
	s+=".cpp \n"
	s+="*/\n"
	s+= "#include<bits/stdc++.h>\n"
	s+= "using namespace std;\n"
	s+= "int main(){\n"
	s+= "\n"
	s+= "return 0;\n"
	s+="}\n"
	name+=".cpp"
	f = open(name,'w')
	f.write(s)
	f.close()
	
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
def sst():
	global stopper
	stopper = False
def runner():
	cm = entry2.get()
	os.system(cm)
#Button
btn2 = tk.Button(text="RUNCMD",width=9,command=runner)
btn2.configure(font=bf,bg="yellow",foreground="black")
btn2.pack(side=tk.RIGHT,padx=10,pady = 20)
cnvs2.create_window(50,120,window = btn2)
# CMD CODE END
#global stopper
sst()
root.mainloop()	
