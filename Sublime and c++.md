<a href="https://www.compromath.com/2017/07/install-sublime-text-3-ubuntu-terminal.html"> Install sublime txt </a>
<a href=""> Install sublime txt </a>
<br>
this the code to build system on sublime 
<br>
<p style="color: red">
<hr>
{<br>
"cmd": ["g++ -std=c++17 $file_base_name.cpp -o $file_base_name && ./$file_base_name < in.in >out.in && python3 test.py > verdict"],<br>
"shell":true,<br>
"working_dir":"$file_path",<br>
 "selector": "source.c, source.c++,source.C++,source.C",<br>
}<br>

</p>
<hr>
<p> " sudo apt-get update <br>
sudo apt-get install terminator " use this code if ubuntu version is less then lts 20.04 </p>
