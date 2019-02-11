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

# %% [markdown]
# # Jupyter Notebook for Power Users <a class="tocSkip">

# %% [markdown]
# # Setup

# %% [markdown]
# # Imports

# %% {"collapsed": true}
# %reset -f
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina' # High-res graphs (rendered irrelevant by svg option below)
# %config InlineBackend.print_figure_kwargs = {'bbox_inches':'tight'} # No extra white space
# %config InlineBackend.figure_format = 'svg' # 'png' is default

import warnings
warnings.filterwarnings('ignore') # Because we are adults
from IPython.core.debugger import set_trace
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# iPyPublish imports
# from ipypublish.scripts.ipynb_latex_setup import *
# from IPython.display import SVG, display, Markdown

# %% [markdown]
# # VS Code and Percent Format demo
# This section left intentionally blank.

# %% {"collapsed": true}


# %% {"collapsed": true}

