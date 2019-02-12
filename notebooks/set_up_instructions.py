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
# # Setting up Jupyter Lab/Notebook

# %% [markdown]
# # Caveats
#
# A few of the referenced functions (e.g., AnovaRM, Markdown calling Python variables, and anything involving live MATLAB or R code) require a little extra set up on one's personal machine, and will not run on a Binder instance of Jupyter. However, most everything else should.

# %% [markdown]
# # Getting set up

# %% [markdown]
# ## [Install Anaconda](https://www.anaconda.com/download/)
# - I'd recommend generally getting the latest version of Python; however, version 3.7 has some compatibility issues with some of my favorite packages, so I am sticking to 3.6 for now.
# - Use commands like this to install multiple versions of python simultaneously:
#     ```bash
#     # install scientific stack for Python 3 and 2. 
#     conda create -n py36 python=3.6 anaconda
#     conda create -n py27 python=2.7 anaconda
#
#     # register py27 kernel - no need for "source" on windows
#     source activate py27
#     ipython kernel install
#
#     # same for py36, and install juptyerhub in the py36 env
#     source activate py36
#     ipython kernel install
#     pip install jupyterhub
#     ```

# %% [markdown]
# ### Optional Psychopy environment (for behavioral scientists)
# - You can even install an environment specifically for [Psychopy](https://www.psychopy.org/) to keep things tidy.
# - Get the appropriate `.yml` file from [Gary Lupyan's github](https://github.com/lupyanlab/lab-computer/tree/master/anaconda-environments)
# - Save it somewhere as, say, `psychopy.yml`
# - Go to that location and run: `conda-env create -f psychopy.yml -n psychopy`
# - After that you can always use it via `source activate psychopy` (no need for `source` on Windows)
# - If `conda` has problems finding the version of the package listed in the `.yml` file, simply edit the file so that it isn't as specific in its version requirements for that package.

# %% [markdown]
# ## Install necessary packages
# - `pip install insert_package_name_here`
# - You might have to preface that with `sudo` if you're on a Mac.
# - Alternatively, use `conda install insert_package_name_here` if you run into issues with pip
# - `conda install -c conda-forge insert_package_name_here` is also an option for certain packages.

# %% [markdown]
# ## Troubleshooting
# In the event that for some reason your Jupyter instance of Python isn't seeing your installed packages, this means that it's probably pointing to the wrong Python or the wrong path. First, diagnose the problem in Jupyter by running `!which python` (on Mac/Linux; `!where python` on Windows) and `import sys; sys.path`. The first command checks where it's looking for Python itself (using the terminal), while the second says where it's looking for packages. These answers should look the same from your own terminal as well -- if the answers differ between Jupyter and your terminal, then you've found your problem.  
# <br><br>
# You should be able to fix either problem by activating your chosen environment, and running `python -m ipykernel install --user`

# %% [markdown]
# ## Useful packages
# You're probably going to want the following packages (though some may already be installed via Anaconda):
# - bokeh
# - holoviews
# - **ipypublish**
#     - For generating scientific manuscripts with Jupyter.
#     - Feel free to use my template and edits to this package available [here](https://github.com/stefanuddenberg/psipypublish).
# - jupyter
# - jupyter_contrib_nbextensions
#     - Run the following command for this after install: `jupyter contrib nbextension install --user`
# - jupyterthemes
#     - Use if you're not happy with the default aesthetics of the notebook
#     - Run at terminal for (most of) my aesthetic setup: `jt -t grade3 -fs 12 -tfs 12 -nfs 115 -cellw 88% -T`
#     - If you don't like it, you can always go back to the default: `jt -r`
# - [**jupytext**](https://github.com/mwouts/jupytext)
#     - Allows you to save your notebook in markdown and .py formats. Extremely useful. 
# - **matlab_kernel** and **pymatbridge**
#     - For using MATLAB
#     - If pymatbridge doesn't work, go to MATLABROOT\extern\engines\python and run `python setup.py install`
# - matplotlib
# - nbopen 
#     - Used to associate .ipynb files with Jupyter in your file manager
#         - Linux/BSD: `python -m nbopen.install_xdg`
#         - Windows: `python -m nbopen.install_win`
#         - Mac: Clone the repository and run `./osx-install.sh`
# - numpy
# - pandas
# - pivottablejs
# - prettypandas
# - qgrid
# - **rpy2**
#     - For using R
#     - More instructions in relevant section below
# - scipy
# - seaborn
# - statsmodels
# - wes
#     - Optional package for Wes Anderson-style color palettes

# %% [markdown]
# ## Open Jupyter notebook from terminal or cmd
# -  Use the commands `jupyter lab` or `jupyter notebook`
#     - Make sure to cd into the directory you want to run it in (or at least a directory *higher* than the one you want; you can't go higher from within the notebook instance)
#     - You can switch between views by navigating to `http://localhost:8888/lab` or `http://localhost:8888/tree` respectively.
#     - The latest version of Jupyter lab at time of writing allows you to have a connected Python console to your notebook, and with [this repo](https://github.com/lckr/jupyterlab-variableInspector) you can even get a variable inspector (a la MATLAB or RStudio). While theming support isn't yet available for Jupyter lab, you can at least override the font settings for notebooks in the user settings.

# %% [markdown]
# # Lab extensions
# Enable useful extensions for Jupyter Lab. It's not as fully featured as Jupyter Notebook, and some may not work depending on your exact installation, but they are still useful.
#
# - [ipywidgets](https://github.com/jupyter-widgets/ipywidgets)
# - [latex](https://github.com/jupyterlab/jupyterlab-latex)
# - [plotly and other renderers](https://github.com/jupyterlab/jupyter-renderers)
# - [table of contents](https://github.com/jupyterlab/jupyterlab-toc)
# - [**variable inspector**](https://github.com/lckr/jupyterlab-variableInspector) — easily one of my favorites, but a little buggy and requires your notebook to be in "Trusted" mode
# - [jupyterlab_html](https://github.com/mflevine/jupyterlab_html) (for displaying HTML files)
# - [jupyterlab_snippets](https://github.com/QuentinAndre/jupyterlab_snippets) — doesn't currently work for me, but boy would it be useful. In the meantime, I've been using an external program called [Cacher](https://www.cacher.io/)
# - [code formatter](https://github.com/ryantam626/jupyterlab_code_formatter) — works great with [Black](https://github.com/ambv/black)
# - [jupyterlab_bokeh](https://github.com/bokeh/jupyterlab_bokeh)
# - [nbdime](https://github.com/jupyter/nbdime) — for diffing notebooks

# %% [markdown]
# ## Notebook extensions (nbextensions)
# Enable your favorite nbextensions for the Notebook view (mine are listed below).
# - Tree Filter
# - table_beautifier
# - Variable inspector
# - Codefolding
# - Codefolding in editor
# - Chrome clipboard
# - contrib_nbextensions_help_item
# - nbextensions dashboard tab
# - Collapsible Headings, with add a control, adjust size of toggle controls, gray bracketed ellipsis, command-mode, collapse with ToC2
# - Python Markdown
#     - must be trusted notebook to use properly -- enable trust at top-right of notebook
# - Table of Contents (2), with auto-number, sidebar, widen display, display toc as navigation menu, move title and menu left instead of center, and collapse
#     - can export notebook to HTML with table of contents with: `jupyter nbconvert --to html_toc FILENAME.ipynb`
#     - if you get an error that says "No such module as 'pre_pymarkdown'", then you will need to do the following:
#         - find "pre_pymarkdown.py" on your computer and add it to the PYTHONPATH environment variable
#         - add the following to your "jupyter_nbconvert_config.py" file:
#         ```python 
#         c = get_config()
#         c.Exporter.preprocessors = ['pre_pymarkdown.PyMarkdownPreprocessor'] 
#         ```
# - [Snippets](https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/snippets)
#     - Can modify `$(jupyter --data-dir)/nbextensions/snippets/snippets.json` to create boilerplate snippets of code or text you can insert into your notebooks (e.g., common imports, common functions, etc.)
#     - Note that this needs to be valid JSON, so you should use a tool list [JSONLint](https://jsonlint.com/) to make sure that your modifications will work.
# - Snippets menu
#     - Has huge list of popular snippets for scientific computing.
# - Hide input
# - Hide input all
#     - Check the documentation on these extensions to see how you can export to HTML and the like while respecting the hidden input!

# %% [markdown]
# ## Slideshow
# You can turn any Jupyter notebook into a slideshow!
# - Set up your slideshow layout for the notebook. From the toolbar: View --> Cell toolbar --> Slideshow
#     - For each cell, use the dropdown box toward the upper right corner to decide if it will be a slide (left-right arrows), sub-slide (up-down arrows), fragment (reveal on further button presses), notes, or skipped.
# - Make sure to have a complete copy of [reveal.js](https://github.com/hakimel/reveal.js/) in the folder with your notebook (in a folder called reveal.js)
# - Run the following from your command line: `jupyter nbconvert FILENAME.ipynb --to slides --reveal-prefix reveal.js`
# - That's it! Now you should have a .slides.html file that works great.
