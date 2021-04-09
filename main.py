import tkinter as tk
import tkinter.font as tkf
import datetime as dt
from datetime import datetime as dts
import os
root = tk.Tk()
root.geometry("720x300")
root.title("TCrator")
root.configure(bg="blue")
#FILE CREATE CODE START

# Label
fn1 = tkf.Font(size=20)
title = tk.Label(root,text="TCrator")
title.configure(bg="blue",foreground="white",font=fn1)
title.pack()
#canvas One
cnvs = tk.Canvas(root,width = 620,height = 150)
cnvs.pack(side=tk.LEFT,pady=30)
cnvs.configure(bg="blue")
#canvas Two
cnvs2 = tk.Canvas(root,width = 100,height = 150)
cnvs2.pack(side=tk.RIGHT,pady=30)
cnvs2.configure(bg="blue")
# Input Box
entry = tk.Entry(root,width=50)
fn2 = tkf.Font(family="Lucida Console")
entry.configure(bg="white",font=fn2)
entry.pack(side=tk.LEFT,padx=10,pady=10)
cnvs.create_window(270,20,window = entry)

#'''
def file_creator():
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
	os.system("subl {}".format(name))
# Button
bf = tkf.Font(size=10)
btn = tk.Button(text="CREATE",width=9,command=file_creator)
btn.configure(font=bf)
btn.pack(side=tk.LEFT,padx=10,pady = 20)
cnvs2.create_window(50,20,window = btn)

#FILE CREATE CODE END
# CMD CODE START
#input box
entry2 = tk.Entry(root,width=50)
fn2 = tkf.Font(family="Lucida Console")
entry2.configure(bg="white",font=fn2)
entry2.pack(side=tk.RIGHT,padx=10,pady=10)
cnvs.create_window(270,80,window = entry2)
def runner():
	cm = entry2.get()
	os.system(cm)
#Button
btn2 = tk.Button(text="RUNCMD",width=9,command=runner)
btn2.configure(font=bf)
btn2.pack(side=tk.RIGHT,padx=10,pady = 20)
cnvs2.create_window(50,80,window = btn2)
# CMD CODE END
root.mainloop()		






















