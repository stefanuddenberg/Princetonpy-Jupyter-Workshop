---
jupyter:
  celltoolbar: Slideshow
  hide_input: false
  jupytext:
    metadata_filter:
      cells:
        additional: all
      notebook:
        additional: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.0'
      jupytext_version: 0.8.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.6.2
  toc:
    nav_menu: {}
    number_sections: true
    sideBar: true
    skip_h1_title: false
    toc_cell: false
    toc_position: {}
    toc_section_display: block
    toc_window_display: false
  varInspector:
    cols:
      lenName: 16
      lenType: 16
      lenVar: 40
    kernels_config:
      python:
        delete_cmd_postfix: ''
        delete_cmd_prefix: 'del '
        library: var_list.py
        varRefreshCmd: print(var_dic_list())
      r:
        delete_cmd_postfix: ') '
        delete_cmd_prefix: rm(
        library: var_list.r
        varRefreshCmd: 'cat(var_dic_list()) '
    types_to_exclude:
    - module
    - function
    - builtin_function_or_method
    - instance
    - _Feature
    window_display: false
---

# Python tips and tricks <a class="tocSkip"></a>


# Inspection


## Get a function's source code

```python
import inspect
import numpy as np

print(inspect.getsource(np))
```

## Find where a function lives

```python
inspect.getfile(np)
```

# Memoization
Can make recursive functions run faster, for example

```python
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    '''Computes the Nth term of the fibonacci sequence'''
    
    # Check that the input is a positive integer
    if type(n) != int or n < 1:
        raise TypeError("n must be a positive integer.")
        
    # Compute the Nth term
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for n in range(1,51):
    print(fibonacci(n))
```

# Miscellany
If you want to start digging deeper into Python, you can [learn some cool things here](https://youtu.be/OSGv2VnC0go), [here](http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html), and [here](https://www.youtube.com/watch?v=7lmCu8wz8ro&index=2&list=PLl_RiCpxqWcAKgcznY3IxZ3ZMRFTvp2Z2).[^1] 

[^1]: [Attendant notebook here](https://github.com/austin-taylor/code-vault/blob/master/python_expert_notebook.ipynb).


# F-strings
Python now has 3 ways to format strings: %-formatting, str.format(), and now f-strings. F-strings are by far my favorite, and I now never use the other two methods unless absolutely necessary. With f-strings, you can place arbitrary code inside of a string using curly braces. Makes writing strings much easier. 

```python
foo = 100
print(f"foo is equal to {foo}")
```

# Tuple unpacking
That said, here is my favorite random snippet of python code ever. You can swap variable values without needing any temporary variables via **tuple unpacking**. 

```python
a = "A"
b = "B"

# Swap!
a, b = b, a 

print(f"a = {a}")
print(f"b = {b}")
```

# Extended iterable unpacking 
Python 3 only.

```python
# grab all the items between first and last item
_, *middle, _ = [1, 2, 3, 4, 5, 6]
print(middle)
```

# List comprehensions
List comprehensions are found all over the place, and allow you to program almost as if you were writing a sentence in English.

```python
colors = ["red", "blue", "green"]
[print(color) for color in colors]
```

# Generator expressions
Like list comprehensions, only lazily evaluated.

```python
# get sum of squares of numbers taken from the range 1 to 10
s = sum(i**2 for i in range(1, 11))
print(s)
```

# Zipping lists

```python
a = ['a', 'b', 'c']
b = [1, 2, 3]

c = zip(a, b)
# zip objects are generators, so lazily evaluated. 
# need to cast into a list if we want to see everything inside
clist = list(c)
print(clist)
```

# Unzipping lists

```python
unzipped = zip(*clist)
print(list(unzipped))
```

# First-class functions
Since functions are first class citizens in Python, you can even assign them to dictionaries! This means you can make a dictionary of functions which you can call later down the line. This opens up a lot of possibilities — use your imagination!

```python
def meow():
    print("meow")

def roar():
    print("roar")

def bark():
    print("bark")

soundDict = {"cat": meow, "dog": bark, "bear": roar}

animals = ["cat", "bear", "cat", "dog"]

for animal in animals:
    soundDict[animal]()
```
