---
jupyter:
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
  rise:
    theme: moon
  toc:
    nav_menu: {}
    number_sections: true
    sideBar: true
    skip_h1_title: false
    toc_cell: false
    toc_position:
      height: 875px
      left: 0px
      right: 1728.63px
      top: 88px
      width: 191.375px
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

# Markdown Tutorial
Double-click on cells to see how they were written!


# Headings
Headings are made with preceding "#" signs. `<h1>` is #, `<h2>` is ##, etc.


# White space
Force new blank lines with `<br>` . Can also place two empty spaces at the end of a line to force a line break.


# Emphasis
*Italics* are made by surrounding a word or phrase with asterisks, or with underscores, _like so_.
<br>

**Bold** words are made by surrounding a word or phrase with 2 asterisks/underscores on each end.
<br>

**_You can make a phrase both bold and italic_** by combining the above, or by using 3 stars/underscores instead.


# Lists
## Unordered Lists
- Dashes make bullets
    - And tabbing first makes a sub-bullet
        - You can also just use a single space instead of a tab character; just be consistent.


## Ordered Lists
1. You can make ordered lists with a number followed by a dot.
2. Here's another point. 


# Blockquotes
> Put a ">" before a line to turn it into a blockquote. 


# Code 
Unhighlighted code goes between backticks: `this is code`
<br>

And you can define blocks of code by sandwiching them between 3 backticks on either end (you can even define syntax highlighting!)
<br>

# ```python
x = [1, 2, 3]
for i in x:
    print(i)
# ```


# Hyperlinks and images
[Hyperlinks go in square brackets](https://www.wikiwand.com/en/Kaizen), with the link itself going in parentheses immediately after (no whitespace allowed between neighboring brackets)!
<br><br>

Images are set up just like hyperlinks, but with an exclamation point in front. The writing in square brackets serves as the alt-text for the image.
<br><br>
![Princeton Psychology Department](https://www.onlinepsychologydegree.info/wp-content/uploads/2015/01/princeton.jpg)


# Embed HTML, including video

```python
%%HTML
<iframe width='560' height='315' src='https://www.youtube.com/embed/HW29067qVWk' frameborder='0' allowfullscreen></iframe>
```

# Live website embedding

```python
# %%HTML
# <iframe src="https://jsfiddle.net/rahonavis75/zpjg8rc4/show/" width="800" height="650">
```

# Latex
Sandwich your LaTeX between two dollar signs. 
<br>
$$
\begin{equation*}
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
\end{equation*}
$$


# Embedding Python code in Markdown
Note that this only works in Jupyter Notebook (not Lab) and only if you have Latex and [Python Markdown](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/python-markdown/readme.html) correctly configured.

```python
foo = 100
```

The value of `foo` is {{foo}}
