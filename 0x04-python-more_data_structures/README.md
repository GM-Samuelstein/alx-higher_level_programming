<h1 align="center">0x04.PYTHON - MORE DATA STRUCTURES: SET, DICTIONARIES</h1>
Here is a summary of what I learnt in this project: 
<ul>
<li>How to use common dictionary methods such as: <code>dict.get(key)</code>, <code>dict.copy( )</code>.</li>
<li>How to use the <code>set( )</code> function.</li>
<li>How to find elements that are common in two given sets.</li>
<li>How to find elements that are not common in two given sets.</li>
<li>How to access only the keys in a dictionary using <code>dict.keys( )</code>.</li>
<li>How to access only the values in a dictionary using <code>dict.values( )</code>.</li>
<li>How to access both the keys and the values in a dictionary at the same time using using <code>dict.items( )</code>.</li>
<li>How to access items nested in a dictionary.</li>
<li>How to create a new key/Value pair OR change the value of a key in a dictionary.</li>
<li>How to delete a key in a dictionary.</li>
<li>How to create a <code>lambda</code> function, and use it together with <code>map</code>, <code>reduce</code>, and <code>filter</code>.</li>
</ul>

|File|Description|
|--|--|
|[0-square_matrix_simple.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/0-square_matrix_simple.py)|A function that computes the square value of all integers of a matrix.|
|[0-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/0-main.py)|A python file that tests the function: <code>def square_matrix_simple(matrix=[]):</code> defined in 0-square_matrix_simple.py.|
|[1-search_replace.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/1-search_replace.py)|A function that replaces all occurrences of an element by another in a new list.|
|[1-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/1-main.py)|A python file that tests the function: <code>def search_replace(my_list, search, replace):</code> defined in 1-search_replace.py.|
|[2-uniq_add.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/2-uniq_add.py)|A function that adds all unique integers in a list (only once for each integer).|
|[2-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/2-main.py)|A python file that tests the function: <code>def uniq_add(my_list=[]):</code> defined in 2-uniq_add.py.|
|[3-common_elements.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/3-common_elements.py)|A function that returns a set of common elements in two sets.|
|[3-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/3-main.py)|A python file that tests the function: <code>def common_elements(set_1, set_2):</code> defined in 3-common_elements.py.|
|[4-only_diff_elements.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/4-only_diff_elements.py)|A function that returns a set of all elements present in only one set.|
|[4-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/4-main.py)|A python file that tests the function: <code>def only_diff_elements(set_1, set_2):</code> defined in 4-only_diff_elements.py|
|[5-number_keys.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/5-number_keys.py)|A function that returns the number of keys in a dictionary.|
|[5-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/5-main.py)|A python file that tests the function: <code>def number_keys(a_dictionary):</code> defined in 5-number_keys.py.|
|[6-print_sorted_dictionary.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/6-print_sorted_dictionary.py)|A function that prints a dictionary by ordered keys.|
|[6-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/6-main.py)|A python file that tests the function: <code>def print_sorted_dictionary(a_dictionary):</code> defined in 6-print_sorted_dictionary.py.|
|[7-update_dictionary.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/7-update_dictionary.py)|A function that replaces or adds key/value in a dictionary.|
|[7-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/7-main.py)|A python file that tests the function: <code>def update_dictionary(a_dictionary, key, value):</code> defined in 7-update_dictionary.py.|
|[8-simple_delete.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/8-simple_delete.py)|A function that deletes a key in a dictionary.|
|[8-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/8-main.py)|A python file that tests the function: <code>def simple_delete(a_dictionary, key=""):</code> defined in 8-simple_delete.py.|
|[9-multiply_by_2.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/9-multiply_by_2.py)|A function that returns a new dictionary with all values multiplied by 2.|
|[9-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/9-main.py)|A python file that tests the function: <code>def multiply_by_2(a_dictionary):</code> defined in 9-multiply_by_2.py.|
|[10-best_score.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/10-best_score.py)|A function that returns a key with the biggest integer value.|
|[10-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/10-main.py)|A python file that tests the function: <code>def best_score(a_dictionary):</code> defined in 10-best_score.py.|
|[11-multiply_list_map.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/11-multiply_list_map.py)|A function that returns a list with all values multiplied by a number without using any loops.|
|[11-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/11-main.py)|A python file that tests the function: <code>def multiply_list_map(my_list=[], number=0):</code> defined in 11-multiply_list_map.py.|
|[12-roman_to_int.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/12-roman_to_int.py)|A function that converts a Roman numeral to an integer.|
|[12-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/12-main.py)|A python file that tests the function: <code>def roman_to_int(roman_string):</code> defined in 12-roman_to_int.py.|
|[100-weight_average.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/100-weight_average.py)|A function that returns the weighted average of all integers tuple <code>(&lt;score&gt;, &lt;weight&gt;)</code>.|
|[100-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/100-main.py)|A python file that tests the function: <code>def weight_average(my_list=[]):</code> defined in 100-weight_average.py.|
|[101-square_matrix_map.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/101-square_matrix_map.py)|A function that computes the square value of all integers of a matrix using <code>map</code>.|
|[101-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/101-main.py)|A python file that tests the function: <code>def square_matrix_map(matrix=[]):</code> defined in 101-square_matrix_map.py.|
|[102-complex_delete.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/102-complex_delete.py)|A function that deletes keys with a specific value in a dictionary.|
|[102-main.py](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/102-main.py)|A python file that tests the function: <code>def complex_delete(a_dictionary, value):</code> defined in 102-complex_delete.py.|
|[103-python.c](https://github.com/GM-Samuelstein/alx-higher_level_programming/blob/master/0x04-python-more_data_structures/103-python.c)|Two C functions that print some basic info about Python lists and Python bytes objects.|
