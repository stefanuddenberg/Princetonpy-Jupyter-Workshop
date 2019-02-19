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
#     version: 3.6.7
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: true
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: false
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: true
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
# # Jupyter Tutorial

# %% [markdown]
# # Cells
#
# - All Jupyter notebooks are made up of _cells_. Cells come in two varieties: _code_ and _markdown_.  
#
# - Code cells contain executable code. Markdown cells contain multimedia information such as explanatory text, website links, images, and video, written in markdown.  
#
# - Both types of cells can be _executed_ using the "play" button in the toolbar toward the top of the notebook, or using the shortcut `Ctrl+Enter` (Windows) or `Cmd+Enter` (Mac).[^1]
#
# - Change the type of cell by using the dropdown box toward the top of the notebook, or using `Esc, M` for markdown and `Esc, Y` for code (that means pressing Escape _then_ M, etc.)
#
# [^1]: Cells can be executed out of order, so best practice when writing a notebook is to ensure that your results are reproducible by running all cells from top to bottom. Requiring that the user run cells out of order is a recipe for disaster.

# %% [markdown]
# # Helpful shortcuts
# All of the below commands are for Windows installations. Mac will likely substitute `Cmd` for `Ctrl`.
# - While coding, `SHIFT+TAB` will bring up help for your current function
# - `Ctrl+Enter` executes the current cell, keeping your focus on it
# - `Ctrl+Shift+Enter` executes the current cell, and moves you down to the next cell
# - `Alt+Enter` executes the current cell AND makes a new one below
# - `Esc` brings you to command mode, where you can do a number of things:
#     - `A` makes a new cell above
#     - `B` makes a new cell below
#     - `D D` (that's `D` twice) deletes a cell
#     - `X` cuts selected cells
#     - `C` copies the cells
#     - `V` pastes the cells
#     - `Y` turns the cell into code
#     - `M` turns the cell into Markdown
# - `CTRL+SHIFT+F` brings up the command palette, with all available commands
#
# <div class="alert alert-block alert-info">
# You can also view and edit such shortcuts from the "Help" menu at the top of the screen in the notebook view, or with the art palette icon at the left of the screen in the lab view.
# </div>

# %% [markdown]
# # Debugging in Jupyter Notebooks
# Use `set_trace()` where you want the debugger to start.<br>
# 'n' moves onto the next line<br>
# 'c' continues execution of the script

# %%
from IPython.core.debugger import set_trace


def increment_value(a):
    a += 1
    set_trace()
    print(a)

    
increment_value(3)

# %% [markdown]
# # Magic commands
# These are useful pieces of code that perform some common operations within Jupyter.

# %% [markdown]
# ## lsmagic
# See all magic commands.

# %%
lsmagic

# %% [markdown]
# ## %who
# See a list of current variables in global scope with . Can also specify a data type thereafter.

# %%
# %who

# %% [markdown]
# ## Terminal commands
# Run any command you would run in your computer's terminal by prefacing the command with `!`

# %%
!conda --version
