from tkinter import *
from tkinter.font import *
import subprocess
import os
root = Tk()
root.geometry("1280x720")
root.title(" MYIDE")
def workspace():
	font_object = Font(family = "Lucida Console",size = 13)
	tb = font_object.measure('    ')
	a = Text(root,width = 92,height = 20,bg = "blue",foreground="YELLOW",font = font_object,cursor = 'xterm #FFFFFF',tabs=tb);
	a.pack()
	return a
def crater():
	a = Entry(root,width = 40)
	a.pack(side=LEFT,padx = 0,pady=0)
	return a
def get_canvas():
	cnvs = Canvas(root,width = 1200,height = 700)
	cnvs.pack(side=LEFT,pady=0)
	#cnvs.configure(bg="blue")
	return cnvs
def file_name_label():
	a = Label(root,text = "File Name")	
	a.pack()
	return a
cnvs = get_canvas();	
lbl_name = file_name_label()
file_name = crater()
code_in_text = workspace()
cnvs.create_window(45,20,window = lbl_name) # Label to create a file
cnvs.create_window(250,20,window = file_name) # file name input box
def write_file():
	nm = file_name.get()
	input_code = code_in_text.get("1.0", END)
	#fl = open(nm,'w+')
	print(len(input_code.replace(' ','')))
	if len(input_code.replace(' ','')) > 1:
		fl = open(nm,'w+')
		fl.write(code_in_text.get("1.0", END))
		fl.close()
	else:
		try:
			fl = open(nm,'r')
			code_in_text.insert(END,fl.read())
			fl.close()
		except:
			fl = open(nm,'w+')
			fl.write(input_code)
			fl.close()
		
	fl.close()
def file_create_button():
	btn = Button(root,width = 10,text = "Open or Save",command = write_file)
	btn.pack(padx = 10)
	return btn
def opn():
	os.system('./creater')
def file_formatter_button():
	btn = Button(root,width = 15,text = 'Open File Creater',command = opn)
	btn.pack(padx = 10)
	return btn
create_file_button = file_create_button()
file_format_button = file_formatter_button()
cnvs.create_window(490,20,window = create_file_button) # file name button
cnvs.create_window(620,20,window = file_format_button) # file format button
cnvs.create_window(510,260,window = code_in_text);
# file input
def input_workspace():
	a = Text(root,width=80,height = 11.5)
	a.configure(bg="blue",foreground='white')
	a.pack(side = LEFT)
	return a
code_input = input_workspace()
cnvs.create_window(325,589,window = code_input)
def sinp():
	inf = open('ins','w')
	inf.write(code_input.get("1.0", 'end-1c'))
	inf.close()
def add_input_btn():
	btn = Button(root,width=10,text="save input",command = sinp)
	btn.pack()
	return btn
def run():
	nm = file_name.get()
	output = open('out','w+')
	ok = True
	try:
		if 'cpp' in nm:
			fln = nm[:len(nm)-4]
			cmd = "g++ {} -o {} ".format(nm,fln)
			os.system(cmd)
			cmd = './{} < ins > out  '.format(fln)
			os.system(cmd)
		elif 'py' in nm:
			cmd = "python3 {} < ins > out".format(nm)
			os.system(cmd)		
	except Exception as e:
		pass		
	a = Text(root,width = 43,height = 10,bg = 'blue',wrap = None)
	a.configure(foreground = 'white')
	a.pack(fill = X)
	cnvs.create_window(840,615,window = a)
	a.insert(END,output.read())
def run_f_btn():
	btn = Button(root,width=10,text="Run File",command = lambda:run())
	btn.pack()
	return btn
save_btn = add_input_btn()
cnvs.create_window(720,510,window = save_btn)
run_btn = run_f_btn()
cnvs.create_window(820,510,window = run_btn)
a = Text(root,width = 43,height = 10,bg = 'blue',foreground='white')
a.pack()
cnvs.create_window(840,615,window = a)

mainloop()
