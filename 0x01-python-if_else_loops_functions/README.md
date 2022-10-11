<h1 align="center">0x01.PYTHON</h1>
IF/ELSE, LOOPS, FUNCTIONS.
<h2>Resources</h2>

<h3>Read</h3>
<ul>
  <li><a href="https://docs.python.org/3/tutorial/controlflow.html">More Control Flow Tools(Python.org)[Chapter 4].</a></li>
  <li><a href="https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3">How to use string formatters in Python3[DigitalOcean].</a></li>
</ul>

<h3>Watch</h3>
<ul>
<li><a href="https://www.youtube.com/watch?v=1QXOd2ZQs-Q">Identation Error.</a></li>
  <li><a href="https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt">Derek Barnas - Learn to Program 2: Looping.</a></li>
</ul>

<h3>Man</h3>
<ul>
  <li>python3</li>
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
<li>What does a function that does not use any <code>return</code> statement return .</li>
<li>Scope of variables.</li>
<li>What’s a traceback.</li>
<li>What are the arithmetic operators and how to use them.</li>
</ul>

<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
  <li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>.</li>
  <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).</li>
  <li>All your files should end with a new line.</li>
  <li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code>.</li>
  <li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory.</li>
  <li>Your code should use the pycodestyle (version <code>2.8.*</code>).</li>
  <li>All your files must be executable.</li>
  <li>The length of your files will be tested using <code>wc</code>.</li>
</ul>

<h3>C Scripts</h3>
<ul>
  <li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>.</li>
  <li>All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options <code>-Wall -Werror -Wextra -pedantic -std=gnu89</code>.</li>
  <li>All your files should end with a new line.</li>
  <li>Your code should use the <code>Betty</code> style. It will be checked using betty-style.pl and betty-doc.pl.</li>
  <li>You are not allowed to use global variables.</li>
  <li>No more than 5 functions per file.</li>
  <li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples.</li>
  <li>The prototypes of all your functions should be included in your header file called <code>lists.h</code>.</li>
  <li>Don’t forget to push your header file.</li>
  <li>All your header files should be include guarded.</li>
</ul>

<h1 align="center">TASKS</h1>

<h2>0. Positive anything is better than negative nothing</h2>
This <a href="https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py">program</a> will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print whether the number stored in the variable <code>number</code> is positive or negative.
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
  <li>The variable <code>number</code> will store a different value every time you will run this program.</li>
  <li>You don’t have to understand what <code>import</code>, <code>random.randint</code> do. Do not touch this code. This line should not change: <code>number = random.randint(-10000, 10000).</code></li>
  <li>The output of the program should be:
    <ul>
      <li>The string <code>Last digit of</code>, followed by</li>
      <li>the number, followed by</li>
      <li>the string <code>is</code>, followed by the last digit of <code>number</code>, followed by
        <ul>
          <li>if the last digit is greater than 5: the string <code>and is greater than 5</code>.</li>
          <li>if the last digit is 0: the string <code>and is 0</code>.</li>
          <li>if the last digit is less than 6 and not 0: the string <code>and is less than 6 and not 0</code>.</li>
        </ul>
      </li>
      <li>followed by a new line.</li>
    </ul>
  </li>
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

<h2>2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game</h2>
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
<ul>
  <li>You can only use one <code>print</code> function with string format.</li>
  <li>You can only use one loop in your code.</li>
  <li>You are not allowed to store characters in a variable.</li>
  <li>You are not allowed to import any module.</li>
</ul>  
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/2-print_alphabet.py">2-print_alphabet.py</a> <br><br>

```
guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$
```

<h2>3. When I was having that alphabet soup, I never thought that it would pay off</h2>

<h2>4. Hexadecimal printing</h2>
<h2>5. 00...99</h2>
<h2>6. Inventing is a combination of brains and materials. The more brains you use, the less material you need</h2>
<h2>7. islower</h2>
<h2>8. To uppercase</h2>
<h2>9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important</h2>
<h2>10. a + b</h2>
<h2>11. a ^ b</h2>
<h2>12. Fizz Buzz</h2>
<h2>13. Insert in sorted linked list</h2>
<h2>14. Smile in the mirror</h2>
<h2>15. Remove at position</h2>
<h2>16. ByteCode -> Python #2</h2>

<h2>Notes</h2>
