<h1 align="center">0x00.PYTHON</h1>
HELLO, WORLD!
<h2>Resources</h2>
<h3>Read</h3>
<ul>
  <li><a href="https://docs.python.org/3/tutorial/index.html">The Python Tutorial(Python.org)</a>(Only the first 3 chapters.)</li>
  <li><a href="https://realpython.com/python-f-strings/">How to use string formatters in Python3</a>(f-strings.)</li>
  <li><a href="https://pypi.org/project/pycodestyle/">Pycodestyle</a></li>
</ul>
<h3>Watch</h3>
<ul>
  <li><a href="https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt">Derek Barnas - Learn to Program</a></li>
</ul>

<h2>Learning Objectives</h2>
<ul>
<li>Why Python programming is awesome.</li>
<li>Who created Python.</li>
<li>Who is Guido van Rossum.</li>
<li>Where does the name ‘Python’ come from.</li>
<li>What is the Zen of Python.</li>
<li>How to use the Python interpreter.</li>
<li>How to print text and variables using <code>print</code>.</li>
<li>How to use strings.</li>
<li>What are indexing and slicing in Python.</li>
<li>What is the official Python coding style and how to check your code with <code>pycodestyle</code>.</li>
</ul>

<h2>Requirements</h2>
<h3>Python Scripts</h3>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>.</li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).</li>
<li>All your files should end with a new line.</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code>.</li>
<li>A <code>README.md</code> file at the root of the repo, containing a description of the repository.</li>
<li>A <code>README.md</code> file, at the root of the folder of this project, is mandatory.</li>
<li>Your code should use the pycodestyle (version <code>2.8.*</code>)</li>
<li>All your files must be executable.</li>
<li>The length of your files will be tested using <code>wc</code>.</li>
<h3>Shell Scripts</h3>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>.</li>
<li>All your scripts will be tested on Ubuntu 20.04 LTS.</li>
<li>All your scripts should be exactly two lines long (<code>wc -l</code> file should print 2).</li>
<li>All your files should end with a new line.</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code>.</li>
<li>All your files must be executable.</li>
<h3>C Scripts</h3>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>.</li>
<li>All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options <code>-Wall -Werror -Wextra -pedantic -std=gnu89</code>.</li>
<li>All your files should end with a new line.</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <code>betty-style.pl</code> and <code>betty-doc.pl</code>.</li>
<li>You are not allowed to use global variables.</li>
<li>No more than 5 functions per file.</li>
<li>The prototypes of all your functions should be included in your header file called <code>lists.h</code>.</li>
<li>All your header files should be include guarded.</li>

<h1 align="center">TASKS</h1>

<h2>0. Run Python file</h2>
Write a Shell script that runs a Python script. <br>
The Python file name will be saved in the environment variable <code>$PYFILE</code>. <br>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/0-run">0-run</a> <br><br>

```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
```

<h2>1. Run inline</h2>
Write a Shell script that runs Python code. <br> 
The Python code will be saved in the environment variable <code>$PYCODE</code>. <br> 
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/1-run_inline">1-run_inline</a> <br><br>

```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
```

<h2>2. Hello, print</h2>
Write a Python script that prints exactly <code>"Programming is like building a multilingual puzzle</code>, followed by a new line.
<ul>
  <li>Use the function <code>print</code>.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/2-print.py">2-print.py</a> <br><br>

```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

<h2>3. Print integer</h2>
Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py">source code</a> in order to print the integer stored in the variable <code>number</code>, followed by <code>Battery street</code>, followed by a new line.
<ul>
  <li> The output of the script should be: 
    <ul> 
      <li>the number, followed by <code>Battery street</code>,</li> 
      <li>followed by a new line.</li>
    </ul>
  </li>
  <li>You are not allowed to cast the variable <code>number</code> into a string.</li>
  <li>Your code must be 3 lines long.</li>
  <li>You have to use f-strings.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/3-print_number.py">3-print_number.py</a> <br><br>

```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$
```
  
<h2>4. Print float</h2>
Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py">source code</a> in order to print the float stored in the variable <code>number</code> with a precision of 2 digits.<br> 
<ul>
  <li> The output of the program should be: 
    <ul> 
      <li><code>Float:</code>, followed by the float with only 2 digits.</li> 
      <li>followed by a new line.</li>
    </ul>
  </li>
  <li>You are not allowed to cast <code>number</code> to string.</li>
  <li>You have to use f-strings.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/4-print_float.py">4-print_float.py</a> <br><br>
<code>
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
</code>
 
<h2>5. Print string</h2>
|Filename|Details|
|---|---|
|[**5-print_string.py**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/5-print_string.py)|Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py)  in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.<br> <ul><li> The output of the program should be: <ul> <li>3 times the value of `str`.</li> <li>followed by a new line.</li><li>followed by the 9 first characters of `str`.</li><li>followed by a new line.</li></ul></li><li>You are not allowed to use any loops or conditional statement.</li><li>Your program should be maximum 5 lines long.</li>|
|[**6-concat.py**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/6-concat.py)|Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`<br><ul><li>You are not allowed to use any loops or conditional statements.</li><li>You have to use the variables `str1` and `str2` in your new line of code.</li><li>Your program should be exactly 5 lines long.</li></ul>|
|[**7-edges.py**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/7-edges.py)|Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py).<br><ul><li>You are not allowed to use any loops or conditional statements.</li><li>Your program should be exactly 8 lines long.</li><li>`word_first_3` should contain the first 3 letters of the variable `word`.</li><li>`word_last_2` should contain the last 2 letters of the variable `word`.</li><li>`middle_word` should contain the value of the variable `word` without the first and last letters.</li></ul>|
|[**8-concat_edges.py**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/8-concat_edges.py)|Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.<br><ul><li>You are not allowed to use any loops or conditional statements.</li><li>Your program should be exactly 5 lines long.</li><li>You are not allowed to create new variables.</li><li>You are not allowed to use string literals.</li></ul>|
|[**9-easter_egg.py**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/9-easter_egg.py)|Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.<br><ul><li>Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)</li></ul>|
|[**10-check_cycle.c**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-check_cycle.c)|**Technical interview preparation:**<br><ul><li>You are not allowed to google anything.</li><li>Whiteboard first.</li><li>This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.</li></ul>Write a function in C that checks if a singly linked list has a cycle in it.<br> <ul><li>Prototype: `int check_cycle(listint_t *list);`</li><li>Return: `0` if there is no cycle, `1` if there is a cycle.</li></ul>Requirements:<br><ul><li>Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`.</li></ul>|
|[**100-write.py**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/100-write.py)|Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.<ul><li>Use the function `write` from the `sys` module.</li><li>You are not allowed to use `print`.</li><li>Your script should print to `stderr`.</li><li>Your script should exit with the status code `1`.</li></ul>|
|[**101-compile**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/101-compile)|Write a script that compiles a Python script file.<br><ul><li>The Python file name will be stored in the environment variable `$PYFILE`.</li><li>The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`).</li></ul>|
|[**102-magic_calculation.py**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/102-magic_calculation.py)|Write the Python function `def magic_calculation(a, b):` that does exactly the same as the Python bytecode below this table. <ul><li>Tips on Python Bytecode can be found [here](https://docs.python.org/3.4/library/dis.html).</li></ul>|
|[**lists.h**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/lists.h)|A header file containing a prototype of all the functions used in the C file.|
|[**Zen**](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/Zen)|The Zen of Python.|

