<h1 align="center">0x01.PYTHON</h1>
IF/ELSE, LOOPS, FUNCTIONS.
<h2>Resources</h2>

<h3>Read</h3>
<ul>
  <li><a href="https://docs.python.org/3/tutorial/index.html">The Python Tutorial(Python.org)</a></li>
  <li><a href="https://www.digitalocean.com/community/tutorials/how-to-write-your-first-python-3-program">Digital Ocean Python Tutorial series</a></li>
</ul>

<h3>Watch</h3>
<ul>
<li><a href="https://www.youtube.com/watch?v=1QXOd2ZQs-Q">Identation Error.</a></li>
  <li><a href="https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt">Derek Barnas - Learn to Program</a></li>
</ul>

<h2>Learning Objectives</h2>
<ul>
<li>Why Python programming is awesome.</li>
<li>Why indentation is so important in Python.</li>
<li>How to use the <code>if, if ... else</code> statements.</li>
<li>How to use comments.</li>
<li>How to affect values to variables.</li>
<li>How to use the <code>while</code> and <code>for</code> loops.</li>
<li>How is Python’s <code>for</code> different from <code>C</code>‘s.</li>
<li>How to use the <code>break</code> and <code>continues</code> statements.</li>
<li>How to use <code>else</code> clauses on loops.</li>
<li>What does the <code>pass</code> statement do, and when to use it.</li>
<li>How to use <code>range</code>.</li>
<li>What is a function and how do you use functions.</li>
<li>What does return a function that does not use any <code>return</code> statement.</li>
<li>Scope of variables.</li>
<li>What’s a traceback.</li>
<li>What are the arithmetic operators and how to use them.</li>
</ul>

<h1 align="center">TASKS</h1>

<h2>0. Positive anything is better than negative nothing</h2>
This <a href="https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py">program</a> will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print whether the number stored in the variable <code>number</code> is positive or negative. <br> 
<ul>
  <li>The variable <code>number</code> will store a different value every time you will run this program.</li>
  <li>You don’t have to understand what <code>import</code>, <code>random. randint</code> do. Do not touch this code.</li>
  <li>
    The output of the program should be:
    <ul>
      <li>
        The number, followed by 
        <ul>
          <li>if the number is greater than 0: <code>is positive</code></li>
          <li>if the number is 0: <code>is zero</code></li>
          <li>if the number is less than 0: <code>is negative</code></li>
        </ul>
      </li>
      <li>followed by a new line.</li>
    </ul>
  </li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/0-positive_or_negative.py">0-positive_or_negative.py</a> <br><br>

```
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/0x01$ 
```

<h2>1. The last digit</h2>
This <a href="https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py">program</a> will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable <code>number</code>. <br>
<ul>
  <li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/1-last_digit.py">1-last_digit.py</a> <br><br>

```
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ 
```
