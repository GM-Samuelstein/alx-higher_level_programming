<h1 align="center">0x06.PYTHON - CLASSES</h1>

Here is a summary of what I learnt in this project: 
<ul>
<li>How to properly document modules, classes and functions using <code>google style python docstrings</code>.</li>
<li>How to define a class.</li>
<li>How to create an instance(object) from a defined class.</li>
<li>How to implement the <code>&#95;&#95;init&#95;&#95;</code> method.</li>
<li>How to add attributes and methods to a class.</li>
<li>How to access and use class attributes and methods.</li>
<li>How to access and use object attributes and methods.</li>
<li>How to use the <code>getattr(object_name, attribute_name[, default_value])</code> function.</li>
<li>How to write getters and setters for attributes the pythonic way.</li>
<li>How to add public, protected and private attributes.</li>
<li>How to implement special methods such as <code>&#95;&#95;str&#95;&#95;</code>, <code>&#95;&#95;repr&#95;&#95;</code>, <code>&#95;&#95;del&#95;&#95;</code>, <code>&#95;&#95;eq&#95;&#95;</code>, <code>&#95;&#95;ne&#95;&#95;</code>, <code>&#95;&#95;gt&#95;&#95;</code>, <code>&#95;&#95;ge&#95;&#95;</code>, <code>&#95;&#95;lt&#95;&#95;</code>, and <code>&#95;&#95;le&#95;&#95;</code>.</li>
<li></li>
<li></li>
</ul>

|File|Description|
|--|--|
|[0-square.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/0-square.py)|An  empty class <code>Square</code> that defines a square.|
|[0-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/0-main.py)|A python file that tests the class: <code>Square:</code> defined in 0-square.py.|
|[1-square.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/1-square.py)|A class <code>Square</code> that defines a square by: <code>(based on 0-square.py)</code>. The class also initializes new square objects with the private attribute <code>size</code>.|
|[1-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/1-main.py)|A python file that tests the class: <code>Square:</code> defined in 1-square.py.|
|[2-square.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/2-square.py)|A class <code>Square</code> that defines a square by: <code>(based on 1-square.py)</code>. The class also validates the type and value of the attribute <code>size</code>, before initializing new square objects.|
|[2-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/2-main.py)|A python file that tests the class: <code>Square:</code> defined in 2-square.py.|
|[3-square.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/3-square.py)|A class <code>Square</code> that defines a square by: <code>(based on 2-square.py)</code>. The class also adds a method <code>def area(self):</code> that computes the area of the square.|
|[3-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/3-main.py)|A python file that tests the class: <code>Square:</code> defined in 3-square.py.|
|[4-square.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/4-square.py)|A class <code>Square</code> that defines a square by: <code>(based on 3-square.py)</code>. The class also provides methods to access and update the private attribute <code>size</code>.|
|[4-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/4-main.py)|A python file that tests the class: <code>Square:</code> defined in 4-square.py.|
|[5-square.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/5-square.py)|A class <code>Square</code> that defines a square by: <code>(based on 4-square.py)</code>. The class also adds a method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>.|
|[5-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/5-main.py)|A python file that tests the class: <code>Square:</code> defined in 5-square.py.|
|[6-square.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/6-square.py)|A class <code>Square</code> that defines a square by: <code>(based on 5-square.py)</code>. The class also adds a new attribute `position`, and validates its type and value before initializing new square objects with the attribute. Additionally, the class modifies the method: <code>def my_print(self):</code> to start printing the square at the position specified by <code>position</code>.|
|[6-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/6-main.py)|A python file that tests the class: <code>Square:</code> defined in 6-square.py.|
|[100-singly_linked_list.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/100-singly_linked_list.py)|A class <code>Node</code> that defines a node of a singly linked list.|
|[100-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/100-main.py)|A python file that tests the class: <code>Node:</code> defined in 100-singly_linked_list.py.|
|[101-square.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/101-square.py)|A class <code>Square</code> that defines a square by: <code>(based on 6-square.py)</code>. The class also adds a method: <code>def &#95;&#95;str&#95;&#95;(self):</code> that has the same behavior as the method: <code>def my_print(self):</code>.|
|[101-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/101-main.py)|A python file that tests the class: <code>Square:</code> defined in 101-square.py.|
|[102-square.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/102-square.py)|A class <code>Square</code> that defines a square by: <code>(based on 4-square.py)</code>. The class also adds methods that allows <code>Square</code> instances to answer to the following comparators based on the square area: <code>==</code>, <code>!=</code>, <code>></code>, <code>>=</code>, <code><</code>, and <code><=</code>.|
|[102-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/102-main.py)|A python file that tests the class: <code>Square:</code> defined in 102-square.py.|
|[103-magic_class.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x06-python-classes/103-magic_class.py)|A python class that does exactly the same as a given python bytecode.|
