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
# # Using R and MATLAB in Jupyter with Python
# N.B. Although Jupyter stands for Julia, Python, and R, R Markdown is really the way to go if you're working with R.

# %% [markdown]
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

# %% [markdown]
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

# %% [markdown]
# Load extension allowing one to run R code from within a Python notebook.

# %%
# %load_ext rpy2.ipython

# %% [markdown]
# Do stuff in R with cell or line magics. "-i" imports to R, "-o" outputs from R back to Python.

# %%
# # %%R
# install.packages("ggplot2", dep=TRUE)
# install.packages("tidyr", dep=TRUE)
# install.packages("dplyr", dep=TRUE)
# install.packages("tidyverse", dep=TRUE)

# %% {"magic_args": "-i df", "language": "R"}
# library("ggplot2")
# ggplot(data = df) + geom_point(aes(x = X, y = Y, color = Letter, size = Z))

# %% [markdown]
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

# %% [markdown]
# ## Example Python to MATLAB pipeline
# Load MATLAB extension for running MATLAB code within a Python notebook.

# %%
# %load_ext pymatbridge

# %% [markdown]
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

# %% [markdown]
# Now, transpose it easily in MATLAB!

# %%
# %%matlab -i a -o a
a = a'

# %% [markdown]
# Finally, check that Python can see the correct value of `a`

# %%
a

# %% [markdown]
# ## Plotting in MATLAB

# %%
# %%matlab
b = linspace(0.01,6*pi,100);
plot(sin(b))
grid on
hold on
plot(cos(b),'r')

# %% [markdown]
# Exit MATLAB when done.

# %%
# %unload_ext pymatbridge

# %% [markdown]
# # Run Javascript code
# Note that Javascript executes as the notebook is opened, even if it's been exported as HTML!

# %% {"language": "javascript"}
# console.log('hey!')
