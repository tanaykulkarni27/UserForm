<a href="https://www.compromath.com/2017/07/install-sublime-text-3-ubuntu-terminal.html"> Install sublime txt </a>
<a href=""> Install sublime txt </a>
<br>
this the code to build system on sublime 
<br>
<p style="color: red">
<hr>
{<br>
"cmd": ["g++", "-std=c++14", "$file", "-o", "${file_path}/${file_base_name}"],<br>
"file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",<br>
"working_dir": "${file_path}",<br>
"selector": "source.c, source.c++, source.cxx, source.cpp",<br>
"variants":<br>
[<br>
{<br>
"name": "Run",<br>
"cmd": ["bash", "-c", "g++ -std=c++14 '${file}' -o '${file_path}/${file_base_name}' && terminator -x bash -c '\"${file_path}/${file_base_name}\" ; read'"]<br>
}<br>
]<br>
}<br>
</p>
<hr>
<p> " sudo apt-get update <br>
sudo apt-get install terminator " use this code if ubuntu version is less then lts 20.04 </p>
