<h1 align="center">0x01.PYTHON</h1>
IF/ELSE, LOOPS, FUNCTIONS.

<h2>Resources</h2>

<h3>Read</h3>
<ul>
  <li><a href="https://docs.python.org/3/tutorial/controlflow.html">More Control Flow Tools[Python.org][Chapter 4].</a></li>
  <li><a href="https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3">How to use string formatters in Python3[DigitalOcean].</a></li>
  <li><a href="https://www.geeksforgeeks.org/string-formatting-in-python/">String formatting in python[GeeksforGeeks].</a></li>
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
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
<ul>
  <li>Print all the letters except <code>q</code> and <code>e</code>.</li>
  <li>You can only use one <code>print</code> function with string format.</li>
  <li>You can only use one loop in your code.</li>
  <li>You are not allowed to store characters in a variable.</li>
  <li>You are not allowed to import any module.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/3-print_alphabt.py">3-print_alphabt.py</a> <br><br>

```
guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$
```

<h2>4. Hexadecimal printing</h2>
Write a program that prints all numbers from <code>0</code> to <code>98</code> in decimal and in hexadecimal (as in the following example).
<ul>
  <li>You can only use one <code>print</code> function with string format.</li>
  <li>You can only use one loop in your code.</li>
  <li>You are not allowed to store numbers or strings in a variable.</li>
  <li>You are not allowed to import any module.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/4-print_hexa.py">4-print_hexa.py</a> <br><br>

```
guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$
```

<h2>5. 00...99</h2>
Write a program that prints numbers from <code>0</code> to <code>99</code>.
<ul>
  <li>Numbers must be separated by <code>,</code>, followed by a space.</li>
  <li>Numbers should be printed in ascending order, with two digits.</li>
  <li>The last number should be followed by a new line.</li>
  <li>You can only use no more than 2 <code>print</code> functions with string format.</li>
  <li>You can only use one loop in your code.</li>
  <li>You are not allowed to store numbers or strings in a variable.</li>
  <li>You are not allowed to import any module.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/5-print_comb2.py">5-print_comb2.py</a> <br><br>

```
guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
guillaume@ubuntu:~/0x01$ 
```

<h2>6. Inventing is a combination of brains and materials. The more brains you use, the less material you need</h2>
Write a program that prints all possible different combinations of two digits.
<ul>
  <li>Numbers must be separated by <code>,</code>, followed by a space.</li>
  <li>The two digits must be different.</li>
  <li><code>01</code> and <code>10</code> are considered the same combination of the two digits <code>0</code> and <code>1</code>.</li>
  <li>Print only the smallest combination of two digits.</li>
  <li>Numbers should be printed in ascending order, with two digits.</li>
  <li>The last number should be followed by a new line.</li>
  <li>You can only use no more than 3 <code>print</code> functions with string format.</li>
  <li>You can only use no more than 2 loops in your code.</li>
  <li>You are not allowed to store numbers or strings in a variable.</li>
  <li>You are not allowed to import any module.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/6-print_comb3.py">6-print_comb3.py</a> <br><br>

```
guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
guillaume@ubuntu:~/0x01$ 
```
<h2>7. islower</h2>
Write a function that checks for lowercase character.
<ul>
  <li>Prototype: <code>def islower(c):</code></li>
  <li>Returns <code>True</code> if <code>c</code> is lowercase.</li>
  <li>Returns <code>False</code> if otherwise.</li>
  <li>You are not allowed to import any module.</li>
  <li>You are not allowed to use <code>str.lower()</code> and <code>str.islower()</code>.</li>
  <li><a href="https://docs.python.org/3.4/library/functions.html?highlight=ord#ord">Tips:ord()</a></li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/7-islower.py">7-islower.py</a> <br><br>

```
guillaume@ubuntu:~/0x01$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

guillaume@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
guillaume@ubuntu:~/0x01$ 
```

<h2>8. To uppercase</h2>
Write a function that prints a string in uppercase followed by a new line.
<ul>
  <li>Prototype: <code>def uppercase(str):</code></li>
  <li>You can only use no more than 2 <code>print</code> functions with string format.</li>
  <li>You can only use one loop in your code.</li>
  <li>You are not allowed to import any module.</li>
  <li>You are not allowed to use <code>str.upper()</code> and <code>str.isupper()</code></li>
  <li><a href="https://docs.python.org/3.4/library/functions.html?highlight=ord#ord">Tips:ord()</a></li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/8-uppercase.py">8-uppercase.py</a> <br><br>

```
guillaume@ubuntu:~/0x01$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")

guillaume@ubuntu:~/0x01$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
guillaume@ubuntu:~/0x01$
```
<h2>9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important</h2>
<h2>10. a + b</h2>
<h2>11. a ^ b</h2>
<h2>12. Fizz Buzz</h2>
<h2>13. Insert in sorted linked list</h2>
<h2>14. Smile in the mirror</h2>
<h2>15. Remove at position</h2>
<h2>16. ByteCode -> Python #2</h2>

<h2>Notes</h2>
