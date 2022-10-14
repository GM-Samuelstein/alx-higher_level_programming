<h1 align="center" id="top">0x00.PYTHON</h1>
HELLO, WORLD!
<h2>Resources</h2>
<h3>Read</h3>
<ul>
  <li><a href="https://docs.python.org/3/tutorial/index.html">The Python Tutorial[Python.org][Chapter 1-3].</a></li>
  <li><a href="https://realpython.com/python-f-strings/">How to use string formatters in Python3[RealPython].</a></li>
  <li><a href="https://pypi.org/project/pycodestyle/">Pycodestyle - Style Guide for Python Code.</a></li>
</ul>
<h3>Watch</h3>
<ul>
  <li><a href="https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt">Derek Barnas - Learn to Program 1</a></li>
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
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
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

```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
```
 
<h2>5. Print string</h2>
Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py">source code</a> in order to print 3 times a string stored in the variable <code>str</code>, followed by its first 9 characters.<br> 
<ul>
  <li> The output of the program should be: 
    <ul> 
      <li>3 times the value of <code>str</code>.</li>
      <li>followed by a new line.</li>
      <li>followed by the 9 first characters of <code>str</code>.</li>
      <li>followed by a new line.</li>
    </ul>
  </li>
  <li>You are not allowed to use any loops or conditional statement.</li>
  <li>Your program should be maximum 5 lines long.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/5-print_string.py">5-print_string.py</a> <br><br>

```
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
```

<h2>6. Play with strings</h2>
Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py">source code</a> to print <code>Welcome to Holberton School!</code><br>
<ul>
  <li>You are not allowed to use any loops or conditional statements.</li>
  <li>You have to use the variables <code>str1</code> and <code>str2</code> in your new line of code.</li>
  <li>Your program should be exactly 5 lines long.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/6-concat.py">6-concat.py</a> <br><br>

```
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
```

<h2>7. Copy - Cut - Paste</h2>
Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py">source code</a>.<br>
<ul>
  <li>You are not allowed to use any loops or conditional statements.</li>
  <li>Your program should be exactly 8 lines long.</li>
  <li><code>word_first_3</code> should contain the first 3 letters of the variable <code>word</code>.</li>
  <li><code>word_last_2</code> should contain the last 2 letters of the variable <code>word</code>.</li>
  <li><code>middle_word</code> should contain the value of the variable <code>word</code> without the first and last letters.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/7-edges.py">7-edges.py</a> <br><br>

```
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$ 
```

<h2>8. Create a new sentence</h2>
Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py">source code</a> to print <code>object-oriented programming with Python</code>, followed by a new line.<br>
<ul>
  <li>You are not allowed to use any loops or conditional statements.</li>
  <li>Your program should be exactly 5 lines long.</li>
  <li>You are not allowed to create new variables.</li>
  <li>You are not allowed to use string literals.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/8-concat_edges.py">8-concat_edges.py</a> <br><br>

```
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 
```

<h2>9. Easter Egg</h2>
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.<br>
<ul>
  <li>Your script should be maximum 98 characters long (please check with <code>wc -m 9-easter_egg.py</code>)</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/9-easter_egg.py">9-easter_egg.py</a> <br><br>

```
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$
```

<h2>10. Linked list cycle</h2>
<b>Technical interview preparation:<b><br>
<ul>
  <li>You are not allowed to google anything.</li>
  <li>Whiteboard first.</li>
  <li>This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.</li>
</ul>
Write a function in C that checks if a singly linked list has a cycle in it.<br>
<ul>
  <li>Prototype: <code>int check_cycle(listint_t *list);</code></li>
  <li>Return: <code>0</code> if there is no cycle, <code>1</code> if there is a cycle.</li>
</ul>
Requirements:<br>
<ul>
  <li>Only these functions are allowed: <code>write</code>, <code>printf</code>, <code>putchar</code>, <code>puts</code>, <code>malloc</code>, <code>free</code>.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-check_cycle.c">10-check_cycle.c</a>, <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/lists.h">lists.h</a> <br><br>

```
carrie@ubuntu:~/0x00$ cat lists.h
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
```
  
```
carrie@ubuntu:~/0x00$ cat 10-linked_lists.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
```
  
```
carrie@ubuntu:~/0x00$ cat 10-main.c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *current;
    listint_t *temp;
    int i;

    head = NULL;
    add_nodeint(&head, 0);
    add_nodeint(&head, 1);
    add_nodeint(&head, 2);
    add_nodeint(&head, 3);
    add_nodeint(&head, 4);
    add_nodeint(&head, 98);
    add_nodeint(&head, 402);
    add_nodeint(&head, 1024);
    print_listint(head);

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    temp = current->next;
    current->next = head;

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    current->next = temp;

    free_listint(head);

    return (0);
}
```
 
```
carrie@ubuntu:~/0x00$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
carrie@ubuntu:~/0x00$$ ./cycle 
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
carrie@ubuntu:~/0x00$
```
  
<h2>11. Hello, write</h2>
Write a Python script that prints exactly <code>and that piece of art is useful - Dora Korpar, 2015-10-19</code>, followed by a new line.
<ul>
  <li>Use the function <code>write</code> from the <code>sys</code> module.</li>
  <li>You are not allowed to use <code>print</code>.</li>
  <li>Your script should print to <code>stderr</code>.</li>
  <li>Your script should exit with the status code <code>1</code>.</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/100-write.py">100-write.py</a> <br><br>
  
```
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ 
```
  
<h2>12. Compile</h2>  
Write a script that compiles a Python script file.
<ul>
  <li>The Python file name will be stored in the environment variable <code>$PYFILE</code>.</li>
  <li>The output filename has to be <code>$PYFILEc</code> (ex: <code>export PYFILE=my_main.py</code> => output filename: <code>my_main.pyc</code>).</li>
</ul>
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/101-compile">101-compile</a> <br><br>
  
```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Best School"
1
guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
guillaume@ubuntu:~/py/0x00$   
```  
  
<h2>13. ByteCode -> Python #1</h2>  
Write the Python function <code>def magic_calculation(a, b):</code> that does exactly the same as the Python bytecode below. 
 
```  
 3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```  
  
<ul>
  <li>Tips on Python Bytecode can be found <a href ="https://docs.python.org/3.4/library/dis.html">here</a>.</li>
</ul>  
File: <a href="https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x00-python-hello_world/102-magic_calculation.py">102-magic_calculation.py</a> <br><br> 

<h2>Notes</h2>
10; 13
<a href="#top>Back to Top</a>
