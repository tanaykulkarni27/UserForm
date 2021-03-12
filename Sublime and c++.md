<a href="https://www.compromath.com/2017/07/install-sublime-text-3-ubuntu-terminal.html"> Install sublime txt </a>
<a href=""> Install sublime txt </a>
<br>
this the code to build system on sublime 
<br>
<p style="color: red">

{ <br> 
   "cmd": "g++ \"${file}\" -o \"${file_path}\\\\${file_base_name}\"",<br>
   "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",<br>
   "working_dir": "${file_path}", <br>
   "selector": "source.c,source.c++,source.cpp",<br>
   "shell":true,<br>
   "variants": [<br>
   { <br>
       "name": "Run",<br>
        "cmd" : ["gnome-terminal -- bash -c \"g++ $file_name ;echo -------------output--------------; ./a.out;echo;echo;  echo Press ENTER to continue; read line;exit; exec bash\""<br>
     ],<br>
   }<br>
 ]<br>
}<br>
</p>
<hr>
<p> " sudo apt-get update <br>
sudo apt-get install terminator " use this code if ubuntu version is less then lts 20.04 </p>
