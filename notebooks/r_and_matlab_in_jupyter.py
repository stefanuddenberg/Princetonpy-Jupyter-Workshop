# -*- coding: utf-8 -*-
# ---
# jupyter:
#   hide_input: false
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
#   rise:
#     theme: moon
#   toc:
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     toc_cell: false
#     toc_position: {}
#     toc_section_display: block
#     toc_window_display: false
#   varInspector:
#     cols:
#       lenName: 16
#       lenType: 16
#       lenVar: 40
#     kernels_config:
#       python:
#         delete_cmd_postfix: ''
#         delete_cmd_prefix: 'del '
#         library: var_list.py
#         varRefreshCmd: print(var_dic_list())
#       r:
#         delete_cmd_postfix: ') '
#         delete_cmd_prefix: rm(
#         library: var_list.r
#         varRefreshCmd: 'cat(var_dic_list()) '
#     types_to_exclude:
#     - module
#     - function
#     - builtin_function_or_method
#     - instance
#     - _Feature
#     window_display: false
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Using R and MATLAB in Jupyter with Python <a class="tocSkip"></a>
# N.B. Although Jupyter stands for Julia, Python, and R, R Markdown is really the way to go if you're working with R.

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Run R code
# Note that this requires running from a Python 3 instance of Jupyter (in my case, at least).

# %% [markdown]
# ## R for Jupyter installation instructions:
# In theory, you should just be able to run this line and be all set, but it didn't work for me: `conda install -c r r-essentials`
# <br><br>
# If that didn't work, go through these steps:
# - In R (not RStudio), run the following:
# ```R
# install.packages('devtools')
# devtools::install_github('IRkernel/IRkernel')
# IRkernel::installspec()  # to register the kernel in the current R installation
# ```
# - make sure you have R added to your PATH (in my case, C:\Program Files\R\R-3.3.3\bin\x64)
#     - _Windows_: Need R_HOME (same path as above) and R_USER (just your windows user name) added as separate environment vars
# - Install libraries like ggplot2 directly into R itself, not RStudio: `install.packages('ggplot2', dependencies=TRUE)`
# - _Mac/Linux_: Run `pip install rpy2` from your command line/terminal
#     - _Windows_: [get appropriate installation from here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2), and run `pip install rpy2‑2.8.6‑cp36‑cp36m‑win_amd64.whl` or whatever your .whl file is called from within the directory that has the file.
#         - You may also need to add the following two directories to your PATH: C:\Anaconda3\Library\mingw-w64\bin; C:\Anaconda3\Library\mingw-w64\lib
# - [See here for further information if needed](https://github.com/IRkernel/IRkernel)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Example Python to R pipeline
# First, make some example data in Python.

# %%
import pandas as pd

df = pd.DataFrame(
    {
        "Letter": ["a", "a", "a", "b", "b", "b", "c", "c", "c"],
        "X": [4, 3, 5, 2, 1, 7, 7, 5, 9],
        "Y": [0, 4, 3, 6, 7, 10, 11, 9, 13],
        "Z": [1, 2, 3, 1, 2, 3, 1, 2, 3],
    }
)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Load extension allowing one to run R code from within a Python notebook.

# %%
# %load_ext rpy2.ipython

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Do stuff in R with cell or line magics. "-i" imports to R, "-o" outputs from R back to Python.
#
# <div class="alert alert-info">
# For some reason, my configuration is stripping the arguments to the cell magic; may be an issue with jupytext (although a previous similar issue was supposedly fixed.) Use `%%R -i df` to make the below code work in the meantime.
# </div>

# %% {"magic_args": "-i df", "language": "R"}
# library("ggplot2")
# ggplot(data = df) + geom_point(aes(x = X, y = Y, color = Letter, size = Z))

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Run MATLAB code

# %% [markdown]
# ## MATLAB for Jupyter Installation
# ```bash
# pip install matlab_kernel
# pip install pymatbridge
# ```
#
# If you're getting a "zmq channel closed" error, open jupyter notebook from a different port when using MATLAB
# ```bash
# jupyter notebook --port=8889
# ```

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Example Python to MATLAB pipeline
# Load MATLAB extension for running MATLAB code within a Python notebook.

# %%
# %load_ext pymatbridge

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Let's try transposing an array from Python in MATLAB, then feeding it back into Python.
# <br>
# First, define an array.

# %%
a = [
    [1, 2],
    [3, 4],
    [5, 6]
]
a

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Now, transpose it easily in MATLAB!

# %%
# %%matlab -i a -o a
a = a'

# %% [markdown] {"slideshow": {"slide_type": "-"}}
# Finally, check that Python can see the correct value of `a`

# %%
a

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Plotting in MATLAB

# %%
# %%matlab
b = linspace(0.01,6*pi,100);
plot(sin(b))
grid on
hold on
plot(cos(b),'r')

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Exit MATLAB when done.

# %%
# %unload_ext pymatbridge

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Run Javascript code
# Note that Javascript executes as the notebook is opened, even if it's been exported as HTML!

# %% {"language": "javascript"}
# console.log('hey!')
