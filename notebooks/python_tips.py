# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     metadata_filter:
#       cells:
#         additional: all
#       notebook:
#         additional: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.2
# ---

# %% [markdown]
# # Python tips and tricks

# %% [markdown]
# ## Get a function's source code

# %%
import inspect
import numpy as np

print(inspect.getsource(np))

# %% [markdown]
# ## Find where a function lives

# %%
inspect.getfile(np)

# %% [markdown]
# ## Memoization
# Can make recursive functions run faster, for example

# %%
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

# %% [markdown]
# ## Miscellany
# If you want to start digging deeper into Python, you can [learn some cool things here](https://youtu.be/OSGv2VnC0go), [here](http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html), and [here](https://www.youtube.com/watch?v=7lmCu8wz8ro&index=2&list=PLl_RiCpxqWcAKgcznY3IxZ3ZMRFTvp2Z2).[^1] 
#
# [^1]: [Attendant notebook here](https://github.com/austin-taylor/code-vault/blob/master/python_expert_notebook.ipynb).

# %% [markdown]
# ## F-strings
# Python now has 3 ways to format strings: %-formatting, str.format(), and now f-strings. F-strings are by far my favorite, and I now never use the other two methods unless absolutely necessary. With f-strings, you can place arbitrary code inside of a string using curly braces. Makes writing strings much easier. 

# %%
foo = 100
print(f"foo is equal to {foo}")

# %% [markdown]
# ### Tuple unpacking
# That said, here is my favorite random snippet of python code ever. You can swap variable values without needing any temporary variables via **tuple unpacking**. 

# %%
a = "A"
b = "B"

# Swap!
a, b = b, a 

print(f"a = {a}")
print(f"b = {b}")

# %% [markdown]
# Extended unpacking is also fun! (Python 3 only.)

# %%
# grab all the items between first and last item
_, *middle, _ = [1, 2, 3, 4, 5, 6]
print(middle)

# %% [markdown]
# ### List comprehensions
# List comprehensions are found all over the place, and allow you to program almost as if you were writing a sentence in English.

# %%
colors = ["red", "blue", "green"]
[print(color) for color in colors]

# %% [markdown]
# ### Generator expressions
# Like list comprehensions, only lazily evaluated.

# %%
# get sum of squares of numbers taken from the range 1 to 10
s = sum(i**2 for i in range(1, 11))
print(s)

# %% [markdown]
# ### Zipping lists

# %%
a = ['a', 'b', 'c']
b = [1, 2, 3]

c = zip(a, b)
# zip objects are generators, so lazily evaluated. 
# need to cast into a list if we want to see everything inside
clist = list(c)
print(clist)

# %% [markdown]
# ### Unzipping lists

# %%
unzipped = zip(*clist)
print(list(unzipped))

# %% [markdown]
# ### First-class functions
# Since functions are first class citizens in Python, you can even assign them to dictionaries! This means you can make a dictionary of functions which you can call later down the line. This opens up a lot of possibilities — use your imagination!

# %%
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