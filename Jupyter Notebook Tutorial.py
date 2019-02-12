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
#   toc:
#     nav_menu:
#       height: 314px
#       width: 303px
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     toc_cell: false
#     toc_position:
#       height: 827px
#       left: 0px
#       right: 1304px
#       top: 92px
#       width: 323px
#     toc_section_display: block
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Jupyter Notebook Tutorial <a class="tocSkip">

# %% [markdown] {"slideshow": {"slide_type": "skip"}}
# # Notes

# %% [markdown] {"slideshow": {"slide_type": "skip"}}
# A few of the referenced functions (e.g., AnovaRM, Markdown calling Python variables, and anything involving live MATLAB or R code) will not run on the Binder instance of Jupyter. However, most everything else should.

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Getting set up

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## [Install Anaconda](https://www.anaconda.com/download/)
# - I'd recommend getting the latest version of Python (version 3.6 at time of writing).
# - Also use this to get all the pythons:
#     ```bash
#     # install everything with Python 2 and 3. 
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

# %% [markdown] {"slideshow": {"slide_type": "skip"}}
# ### Troubleshooting

# %% [markdown] {"slideshow": {"slide_type": "skip"}}
# In the event that for some reason your Jupyter instance of Python isn't seeing your installed packages, this means that it's probably pointing to the wrong Python or the wrong path. First, diagnose the problem in Jupyter by running `!which python` (on Mac/Linux) and `import sys; sys.path`. The first command checks where it's looking for Python itself (using the terminal), while the second says where it's looking for packages. These answers should look the same from your own terminal as well -- if the answers differ between Jupyter and your terminal, then you've found your problem. 
# <br><br>
# You should be able to fix either problem by activating your chosen environment, and running `python -m ipykernel install --user`

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Install necessary packages
# - `pip install insert_package_name_here`
# - You might have to preface that with `sudo` if you're on a Mac.
# - Alternatively, use `conda install insert_package_name_here` if you run into issues with pip
# - `conda install -c conda-forge insert_package_name_here` is also an option for certain packages.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Optional packages
# - **You're probably going to want the following packages (though some may already be installed via Anaconda):**
#     - bokeh
#     - holoviews
#     - jupyter
#     - jupyter_contrib_nbextensions
#         - Run the following command for this after install: `jupyter contrib nbextension install --user`
#     - jupyterthemes
#         - Use if you're not happy with the default aesthetics of the notebook
#         - Run at terminal for (most of) my aesthetic setup: `jt -t grade3 -fs 12 -tfs 12 -nfs 115 -cellw 88% -T`
#         - If you don't like it, you can always go back to the default: `jt -r`
#     - **matlab_kernel** and **pymatbridge**
#         - For using MATLAB
#         - If pymatbridge doesn't work, go to MATLABROOT\extern\engines\python and run `python setup.py install`
#     - matplotlib
#     - nbopen 
#         - Used to associate .ipynb files with Jupyter in your file manager
#             - Linux/BSD: `python -m nbopen.install_xdg`
#             - Windows: `python -m nbopen.install_win`
#             - Mac: Clone the repository and run `./osx-install.sh`
#     - numpy
#     - pandas
#     - pivottablejs
#     - prettypandas
#     - qgrid
#     - **rpy2**
#         - For using R
#         - More instructions in relevant section below
#     - scipy
#     - seaborn
#     - statsmodels
#     - wes
#         - Optional package for Wes Anderson-style color palettes

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Optional Psychopy environment
# - **You can even create a Psychopy environment**:
#     - Get the appropriate `.yml` file from [Gary Lupyan's github](https://github.com/lupyanlab/lab-computer/tree/master/anaconda-environments)
#     - Save it somewhere as, say, `psychopy.yml`
#     - Go to that location and run: `conda-env create -f psychopy.yml -n psychopy`
#     - After that you can always use it via `source activate psychopy` (no need for `source` on Windows)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Open Jupyter notebook from terminal or cmd
# - `jupyter lab` or `jupyter notebook`
#     - Make sure to cd into the directory you want to run it in (or at least a directory *higher* than the one you want; you can't go higher from within the notebook instance, nor can you go laterally!)
#     - You can switch between views by navigating to `http://localhost:8888/lab` or `http://localhost:8888/tree` respectively.
#     - The latest version of Jupyter lab at time of writing allows you to have a connected Python console to your notebook, and with [this repo](https://github.com/lckr/jupyterlab-variableInspector) you can even get a variable inspector (a la MATLAB or RStudio). While theming support isn't yet available for Jupyter lab, you can at least override the font settings for notebooks in the user settings.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## nbextensions    
# - **Enable your favorite nbextensions (below I've listed mine).**
#     - Tree Filter
#     - table_beautifier
#     - Variable inspector
#     - Codefolding
#     - Codefolding in editor
#     - Chrome clipboard
#     - contrib_nbextensions_help_item
#     - nbextensions dashboard tab
#     - Collapsible Headings, with add a control, adjust size of toggle controls, gray bracketed ellipsis, command-mode, collapse with ToC2
#     - Python Markdown
#         - must be trusted notebook to use properly -- enable trust at top-right of notebook
#     - Table of Contents (2), with auto-number, sidebar, widen display, display toc as navigation menu, move title and menu left instead of center, and collapse
#         - can export notebook to HTML with table of contents with: `jupyter nbconvert --to html_toc FILENAME.ipynb`
#         - if you get an error that says "No such module as 'pre_pymarkdown'", then you will need to do the following:
#             - find "pre_pymarkdown.py" on your computer and add it to the PYTHONPATH environment variable
#             - add the following to your "jupyter_nbconvert_config.py" file:
#             ```python 
#             c = get_config()
#             c.Exporter.preprocessors = ['pre_pymarkdown.PyMarkdownPreprocessor'] 
#             ```
#     - [Snippets](https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/snippets)
#         - Can modify `$(jupyter --data-dir)/nbextensions/snippets/snippets.json` to create boilerplate snippets of code or text you can insert into your notebooks (e.g., common imports, common functions, etc.)
#         - Note that this needs to be valid JSON, so you should use a tool list [JSONLint](https://jsonlint.com/) to make sure that your modifications will work.
#     - Snippets menu
#         - Has huge list of popular snippets for scientific computing.
#     - Hide input
#     - Hide input all
#         - Check the documentation on these extensions to see how you can export to HTML and the like while respecting the hidden input!

# %% [markdown]
# ## Slideshow
# - **You can turn any Jupyter notebook into a slideshow!**
#     - Set up your slideshow layout for the notebook. From the toolbar: View --> Cell toolbar --> Slideshow
#         - For each cell, use the dropdown box toward the upper right corner to decide if it will be a slide (left-right arrows), sub-slide (up-down arrows), fragment (reveal on further button presses), notes, or skipped.
#     - Make sure to have a complete copy of [reveal.js](https://github.com/hakimel/reveal.js/) in the folder with your notebook (in a folder called reveal.js)
#     - Run the following from your command line: `jupyter nbconvert FILENAME.ipynb --to slides --reveal-prefix reveal.js`
#     - That's it! Now you should have a .slides.html file that works great.

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Markdown Tutorial
# Double-click on the cells to see how everything was written!

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Headings
# Headings are made with preceding "#" signs. `<h1>` is #, `<h2>` is ##, etc.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## White space
# Force new blank lines with `<br>` .

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Emphasis
# *Italics* are made by surrounding a word or phrase with asterisks, or with underscores, _like so_.
# <br>
#
# **Bold** words are made by surrounding a word or phrase with 2 asterisks on each end.
# <br>
#
# **_You can make a phrase both bold and italic_** by combining the above!

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Unordered Lists
# - Dashes make bullets
#     - And tabbing first makes a sub-bullet
#         - You can also just use a single space instead of a tab character; just be consistent.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Ordered Lists
# 1. You can make ordered lists with a number followed by a dot.
# 2. Here's another point. 

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Blockquotes
# > Put a ">" before a line to turn it into a blockquote. 

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Code 
# Unhighlighted code goes between backticks: `this is code`
# <br>
#
# And you can define blocks of code by sandwiching them between 3 backticks on either end (you can even define syntax highlighting!)
# <br>
#
# ```python
# x = [1, 2, 3]
# for i in x:
#     print(i)
# ```

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Hyperlinks and images
# [Hyperlinks go in square brackets](https://www.wikiwand.com/en/Kaizen), with the link itself going in parentheses immediately after (no whitespace allowed between neighboring brackets)!
# <br><br>
#
# Images are set up just like hyperlinks, but with an exclamation point in front. The writing in square brackets serves as the alt-text for the image.
# <br><br>
# ![Yale Psychology Department](http://psychology.yale.edu/sites/default/files/styles/adaptive/public/yalearchitecture_sss2.jpg?itok=jc7f5qWZ)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Embed HTML, including video

# %% {"slideshow": {"slide_type": "subslide"}}
# %%HTML
<iframe width='560' height='315' src='https://www.youtube.com/embed/HW29067qVWk' frameborder='0' allowfullscreen></iframe>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### This works for live websites, too!

# %% {"collapsed": true, "slideshow": {"slide_type": "subslide"}}
# # %%HTML
# <iframe src="https://fiddle.jshell.net/rahonavis75/ed4486f9/show/" width="800" height="500">

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## LaTeX

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Sandwich your LaTeX between two dollar signs. 
# <br>
# $$
# \begin{equation*}
# \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
# \end{equation*}
# $$

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# If you wanted you could literally write your paper in Jupyter notebook! To do this, you would collapse your analysis script with your manuscript by feeding the results of the fomer directly into the latter. Here's an example where I feed a variable into a Markdown cell.

# %% {"collapsed": true, "slideshow": {"slide_type": "subslide"}}
foo = 100

# %% [markdown] {"slideshow": {"slide_type": "fragment"}, "variables": {"foo": "<p><strong>NameError</strong>: name &#39;foo&#39; is not defined</p>\n"}}
# foo is {{foo}}

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Jupyter commands

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Magic commands

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# See all commands.

# %% {"hide_input": false, "slideshow": {"slide_type": "subslide"}}
lsmagic

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# See list of current variables in global scope. Can also specify a data type thereafter.

# %% {"slideshow": {"slide_type": "subslide"}}
# %who

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Terminal commands
# And run terminal commands directly with "!"

# %% {"slideshow": {"slide_type": "subslide"}}
!pip list

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Helpful shortcuts

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# - While coding, `SHIFT+TAB` will bring up help for your current function
# - `CTRL+Enter` executes the current cell, keeping your focus on it
# - `CTRL+SHIFT+Enter` executes the current cell, and moves you down to the next cell
# - `ALT+Enter` executes the current cell AND makes a new one below
# - `ESC` brings you to command mode, where you can do a number of things:
#     - `A` makes a new cell above
#     - `B` makes a new cell below
#     - `D D` (that's `D` twice) deletes a cell
#     - `X` cuts selected cells
#     - `C` copies the cells
#     - `V` pastes the cells
#     - `Y` turns the cell into code
#     - `M` turns the cell into Markdown
# - `CTRL+SHIFT+F` brings up the command palette, with all available commands
# <div class="alert alert-block alert-info">
# You can also view and edit such shortcuts from the "Help" menu at the top of the screen
# </div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Beginner data analysis with pandas

# %% [markdown] {"slideshow": {"slide_type": "skip"}}
# ## In-depth pandas tutorial
# [Giant pandas tutorial](https://www.youtube.com/watch?v=mwt3BTkStNg&t=3s) and [attendant notes](https://github.com/chendaniely/scipy-2017-tutorial-pandas![image.png](attachment:image.png) available at the links.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Setup
# Allow plots in the notebook itself, and enable some helpful functions.

# %% {"slideshow": {"slide_type": "fragment"}}
# %reset -f
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina' # High-res graphs (rendered irrelevant by svg option below)
# %config InlineBackend.print_figure_kwargs = {'bbox_inches':'tight'} # No extra white space
# %config InlineBackend.figure_format = 'svg' # 'png' is default

import warnings
warnings.filterwarnings('ignore') # Because we are adults

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Import example data.

# %% {"scrolled": true, "slideshow": {"slide_type": "fragment"}}
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = sns.load_dataset('tips')
data.head() # show first n entries (default is 5)

# %%
from prettypandas import PrettyPandas

new_table = PrettyPandas(data[['total_bill', 'sex']])
new_table

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Data exploration

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Change default graph appearance to something you like. [See here for full list of available built-in styles.](https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html)

# %% {"collapsed": true, "slideshow": {"slide_type": "fragment"}}
sns.set_style("ticks") # e.g., ggplot, whitegrid, etc.

## Define custom color palette
# flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
# sns.set_palette(flatui)
# sns.palplot(sns.color_palette())

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Plot histograms of tips grouped by sex side by side. Make sure both have the same x and y limits.

# %% {"scrolled": false, "slideshow": {"slide_type": "fragment"}}
data['tip'].hist(by=data['sex'], sharex=True, sharey=True)
sns.despine() # Remove top and right side of box

plt.show() # Somewhat redundant in this context, but suppresses annoying text output.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Plot overlaid histograms.

# %% {"slideshow": {"slide_type": "fragment"}}
grouped_by_sex = data.groupby('sex')

# You can also add several arguments below like bins=20, or normed=True
figure, axes = grouped_by_sex['tip'].plot(kind='hist', normed=False, alpha=.5, legend=True) 

# Re-label legend entries, move legend to right-middle
axes.legend(['Men', 'Women'], loc=(0.75, 0.5)) 

sns.despine()
plt.show()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Show summary stats for the sexes.

# %% {"slideshow": {"slide_type": "fragment"}}
grouped_by_sex['tip'].describe()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Get a subset of the data — here the tips given on Sunday at dinner time.

# %% {"collapsed": true, "slideshow": {"slide_type": "fragment"}}
sunday_dinner_tips = data.tip[(data.day=="Sun") & (data.time=="Dinner")]

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Data processing

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Add a new column showing the percentage of the total bill tipped using a lambda expression. Naturally, you can also accomplish this by defining a named function.

# %% {"slideshow": {"slide_type": "fragment"}}
data['tip_percentage'] = data.apply(lambda row: row['tip']/row['total_bill']*100, axis=1)
data.head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Delete that new column.

# %% {"slideshow": {"slide_type": "fragment"}}
del data['tip_percentage']
data.head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## ANOVA
# <br>
# Perform an ANOVA, using R-style syntax.

# %% {"slideshow": {"slide_type": "fragment"}}
import statsmodels.api as sm
from statsmodels.formula.api import ols

model = 'tip ~ sex * smoker'
lm = ols(model, data=data).fit() 
# lm.summary() # to show regression results
table = sm.stats.anova_lm(lm, typ=2)

display(table)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Make the table prettier and more intelligible.

# %% {"slideshow": {"slide_type": "fragment"}}
from prettypandas import PrettyPandas 

def color_significant_green(val, alpha=0.05):
    if val < alpha: color = 'green'
    else: color = 'black'
    return 'color: %s' % color

def bold_significant(val, alpha=0.05):
    if val < alpha: font_weight = 'bold'
    else: font_weight = 'normal'
    return 'font-weight: %s' % font_weight

t = PrettyPandas(table)
(
    t.applymap(color_significant_green, alpha=.05, subset=['PR(>F)']) # alpha is optional here, of course
    .applymap(bold_significant, alpha=.05, subset=['PR(>F)'])
    .format("{:.3f}", subset=['sum_sq', 'F', 'PR(>F)']) # show only 3 decimal places
)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## T-tests

# %% {"slideshow": {"slide_type": "fragment"}}
from numpy import sqrt
from scipy.stats import ttest_ind

def cohens_d(t, n):
    return 2*t / sqrt(n - 2)

# Set up empty results table
columns = ['n', 't', 'p', 'd']
index = []
results = pd.DataFrame(index=index, columns=columns)

# Get data for t-test
male_tips = data[data['sex']=='Male']['tip']
female_tips = data[data['sex']=='Female']['tip']

# Perform t-test and surrounding calculations
n = male_tips.count() + female_tips.count()
df = n-2
t, p = ttest_ind(male_tips, female_tips)
d = cohens_d(t, n)

# Add data to table
comparison = 'Male vs. Female'
results.loc[comparison] = [n, t, p, d]

# Output pretty table
r = PrettyPandas(results)
(
    r.applymap(color_significant_green, subset=['p'])
    .applymap(bold_significant, subset=['p'])
    .format("{:.3f}", subset=['t', 'p', 'd'])
)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Publication-ready statistics with Markdown

# %% {"slideshow": {"slide_type": "fragment"}}
from IPython.display import Markdown

inequality_symbol = "="
def report_t_test(df, t, p, d, alpha=.001):
    if p < alpha:
        p = .001
        inequality_symbol = "<"
    else:
        inequality_symbol = "="
        
    T = format(t, '.2f').lstrip('0') # 2 decimal places, no leading 0
    P = format(p, '.3f').lstrip('0') 
    D = format(d, '.3f').lstrip('0') 
    DF = format(df, 'd') # integer
    
    output = ('*t*({0})={1}, *p*' + inequality_symbol + '{2}, *d*={3}').format(DF, T, P, D)
    display(Markdown(output))

report_t_test(df, t, p, d)

# %% [markdown] {"slideshow": {"slide_type": "fragment"}, "variables": {"format(d, '.3f').lstrip('0')": "<p><strong>NameError</strong>: name &#39;d&#39; is not defined</p>\n", "format(p, '.3f').lstrip('0')": "<p><strong>NameError</strong>: name &#39;p&#39; is not defined</p>\n", "format(t, '.2f').lstrip('0')": "<p><strong>NameError</strong>: name &#39;t&#39; is not defined</p>\n", "inequality_symbol": "<p><strong>NameError</strong>: name &#39;inequality_symbol&#39; is not defined</p>\n", "n-2": "<p><strong>NameError</strong>: name &#39;n&#39; is not defined</p>\n"}}
# And in plain markdown:
# *t*({{n-2}})={{format(t, '.2f').lstrip('0')}}, *p*{{inequality_symbol}}{{format(p, '.3f').lstrip('0')}}, *d*={{format(d, '.3f').lstrip('0')}}
#
# <div class="alert alert-block alert-info">
# Note that you can copy paste such outputs directly into Word with no loss of formatting!
# </div>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Repeated measures ANOVA
# Requires development version of `statsmodels` package, [available here](https://github.com/statsmodels/statsmodels).
#
# - Install using `pip install git+insert_link_here`
# - *Windows requirements:*
#     - [Git for Windows](https://git-scm.com/download/win)
#     - Latest version of [Visual C++](http://landinghub.visualstudio.com/visual-cpp-build-tools)
# - [Alternate method of doing RM-ANOVA in Python here](https://www.marsja.se/two-way-anova-repeated-measures-using-python/)

# %% {"slideshow": {"slide_type": "fragment"}}
import pandas as pd
import numpy as np
import statsmodels
from statsmodels.stats.anova import AnovaRM
statsmodels.__version__

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Create simulated reaction time data for 2 levels of an independent variable.

# %% {"collapsed": true, "slideshow": {"slide_type": "fragment"}}
N = 20
P = [1,2]

values = [998,511]
 
sub_id = [i+1 for i in range(N)]*len(P)
mus = np.concatenate([np.repeat(value, N) for value in values]).tolist()
rt = np.random.normal(mus, scale=112.0, size=N*len(P)).tolist()
iv = np.concatenate([np.array([p]*N) for p in P]).tolist()

df = pd.DataFrame({'id': sub_id, 'rt': rt, 'iv':iv})

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Do the repeated measures ANOVA.

# %% {"slideshow": {"slide_type": "fragment"}}
aovrm = AnovaRM(df, depvar='rt', subject='id', within=['iv'])
fit = aovrm.fit()
fit.summary()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Plots

# %% [markdown] {"slideshow": {"slide_type": "skip"}}
# ## [Matplotlib tutorial](https://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Line graph with matplotlib
# Plot simple line graph with sample data.

# %% {"slideshow": {"slide_type": "fragment"}}
line_data = range(1,10)

plt.figure()
plt.title("Example Graph", size="xx-large") # can also feed font point size, like 36
plt.xlabel("X-Axis Label", size="x-large")
plt.ylabel("Y-Axis Label", size="x-large")
plt.xlim(0,10)
plt.ylim(0,10)
plt.plot(line_data, 'b*-', markersize=10, linewidth=3, label='Sample Data') # b*- means blue star marker with line
plt.tick_params(axis="both", which="major", labelsize=14)
plt.legend(loc=(0.25, 0.75), scatterpoints=1)
plt.show()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Line graph with Seaborn
# Plot Anscombe's quartet.

# %% {"slideshow": {"slide_type": "fragment"}}
import seaborn as sns
sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
anscombe = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
# Semi-colon suppresses the non-graph output
ax = sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=anscombe,
                col_wrap=2, ci=None, palette="muted", size=4,
                scatter_kws={"s": 50, "alpha": 1}); 

# Change axis labels
ax.set(xlabel='X', ylabel='Y');

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Bar graph
#
# Naturally, this defaults to showing a 95% confidence interval.

# %% {"slideshow": {"slide_type": "fragment"}}
ax = sns.barplot(x="day", y="total_bill", data=data, capsize=0.1)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Subplots — Violin plot and beeswarm plot
#
# Plot violin plot with overlaid beeswarm plot.

# %% {"slideshow": {"slide_type": "fragment"}}
fig, ax = plt.subplots()

# Output to the size of A4 paper
fig.set_size_inches(11.7, 8.27)

# Overlay a swarmplot on top of a violinplot
ax = sns.violinplot(x="day", y="total_bill", data=data, inner=None)
ax = sns.swarmplot(x="day", y="total_bill", data=data, color="white")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Factor Plots

# %% {"slideshow": {"slide_type": "fragment"}}
def set_titles(thisPlot, titleList, fontSize):
    for ax, title in zip(thisPlot.axes.flat, titleList):
        ax.set_title(title, fontsize=fontSize)

        
def set_labels(thisPlot, xLabel, yLabel, fontSize):
    thisPlot.set_xlabels(xLabel, fontsize=fontSize)
    thisPlot.set_ylabels(yLabel, fontsize=fontSize)

    
def set_xtick_labels(thisPlot, tickList, fontSize):
    thisPlot.set_xticklabels(tickList, fontsize=fontSize)

    
def set_legend(thisPlot, legendEntries, fontSize):
    # find where last graph is so we can put the legend there
    maxIndex = max(thisPlot.axes.shape) - 1
    
    # format the legend, placing it outside the axes
    thisPlot.axes[0][maxIndex].legend(bbox_to_anchor=(1.05, 1), loc=2, 
                                      fontsize=fontSize, borderaxespad=0.)
    legend = thisPlot.axes[0][maxIndex].get_legend()
    labels = legend.get_texts()
    for i, thisLabel in enumerate(labels):
        labels[i].set_text(legendEntries[i])        


# Make plots -- many of these arguments are optional
barPlot = sns.factorplot(x="day", y="total_bill", hue="sex", 
                         col="time", kind="bar", data=data, 
                         size=5, aspect=1, legend=False)

beeswarmPlot = sns.factorplot(x="day", y="total_bill", hue="sex", 
                              col="time", kind="swarm", dodge=True,
                              data=data, size=5, aspect=1, legend=False)

# Format them nicely!
# Axis labels
xLabel = ""# "Day"
yLabel = "Total Bill"
set_labels(barPlot, xLabel, yLabel, 20)
set_labels(beeswarmPlot, xLabel, yLabel, 20)

# Titles
title_list = ["Lunch", "Dinner"]
titles = [x.title() for x in title_list] # ["Bimodal", "Normal", "Skewed"]
set_titles(barPlot, titles, 30)
set_titles(beeswarmPlot, titles, 30)

# X axis tick labels or category labels
x_tick_labels = ["Thursday", "Friday", "Saturday", "Sunday"]
set_xtick_labels(barPlot, x_tick_labels, 15)
set_xtick_labels(beeswarmPlot, x_tick_labels, 15)

# Change legends
legendEntries = ["Male", "Female"]
set_legend(barPlot, legendEntries, 15)
set_legend(beeswarmPlot, legendEntries, 15)

# Save plots
# barPlot.savefig("barPlot.svg") # can also use other extensions, like .png
# beeswarmPlot.savefig("beePlot.svg")

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Interactive Plots
#

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Bokeh
#
# Made using bokeh. [See here for a great tutorial](https://www.youtube.com/watch?v=6Pzg-UY1VDg&index=9&t=1393s&list=PLl_RiCpxqWcAKgcznY3IxZ3ZMRFTvp2Z2), and [here for the attendant notebook](https://github.com/claresloggett/demo_visualisation_pyconau2017). Code below adapted from linked code to our current dataset.

# %% {"slideshow": {"slide_type": "fragment"}}
from bokeh.plotting import figure, output_notebook, show

this_plot= figure(width=600, height=600)

this_plot.circle(x=data['total_bill'], y=data['tip'], size=10, alpha=0.7)
output_notebook() # to output inline 
show(this_plot)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Make better, more interactive plot. Let's plot a scatterplot of tip amount vs. total bill, separately for men and women.
#
# [See here for more information on styling Bokeh plots.](https://bokeh.pydata.org/en/latest/docs/user_guide/styling.html)

# %% {"slideshow": {"slide_type": "fragment"}}
from bokeh.plotting import figure, output_notebook, show, ColumnDataSource
import bokeh.models.tools as tools

# Get relevant subsets of data
male_data = data[data['sex'] == 'Male']
female_data = data[data['sex'] == 'Female']

# Convert to format bokeh understands
source_male = ColumnDataSource(male_data)
source_female = ColumnDataSource(female_data)

# Set up figure
this_plot = figure(width=600, height=600)

this_plot.circle(source=source_male, x='total_bill', y='tip', color='teal',
         size=10, alpha=0.7, legend='Men')

this_plot.circle(source=source_female, x='total_bill', y='tip', color='darkorange',
         size=10, alpha=0.7, legend='Women')

# Set axis labels
this_plot.xaxis.axis_label = "Total Bill"
this_plot.yaxis.axis_label = "Tip Amount"

# Show information when hovering the mouse over datapoints
this_plot.add_tools(tools.HoverTool(tooltips=[('Day', '@day')])) # use @ to choose feature from dataset

# Hide all circles of a given category when clicked in legend
this_plot.legend.click_policy = 'hide' 

output_notebook() 
show(this_plot)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Dropdown menus with Holoviews

# %% {"slideshow": {"slide_type": "fragment"}}
import holoviews as hv
hv.extension('bokeh', 'matplotlib')

ds = hv.Dataset(data, kdims=["sex", "smoker", "total_bill"],
                      vdims=["time", "size", "day", "tip"])

# %% {"slideshow": {"slide_type": "fragment"}}
# %%output backend='bokeh'
# %%output size=200
# %%opts Scatter [tools=['hover']] (size=8 alpha=0.5)

kdims=["tip"]
vdims=["total_bill", "day", "time", "size"] # include "smoker" if you don't want it as drop-down choice

# Scatter plot with hover tool that includes all the things
scatter = ds.to(hv.Scatter, kdims, vdims).overlay('sex')
scatter

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Pivot table plots

# %% {"scrolled": false, "slideshow": {"slide_type": "fragment"}}
from pivottablejs import pivot_ui
pivot_ui(data)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Interactive slider

# %% {"slideshow": {"slide_type": "fragment"}}
import matplotlib.pyplot as plt
from ipywidgets import *
from numpy import pi, arange, sin

t = arange(0, 1.0, 0.01)


def pltsin(f):
    plt.plot(t, sin(2*pi*t*f))
    plt.show()
    
interact(pltsin, f=(1,10,0.1))

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Plotly
# [Plotly](https://plot.ly/products/dash/) is another package for producing really nice and interactive graphs, but it requires signing up for an account to initialize it. After initialization you can use it online by default (which means all of your graphs get saved to the cloud for everyone to see forever) or you can use it offline (as demoed below). Examples taken or modified from [here](https://plot.ly/python/ipython-notebook-tutorial/).

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Setup and basic line graph

# %% {"slideshow": {"slide_type": "fragment"}}
import plotly
# plotly.tools.set_credentials_file(username='XXX', api_key='XXX') # initialize with your credentials -- only need to do once ever.
from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

plotly.offline.iplot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})

# %% [markdown] {"slideshow": {"slide_type": "notes"}}
# ### Troubleshooting setup
# When I first tried using plotly I sometimes got `"IOPub data rate exceeded"` errors. Here's how you fix that:
# - run ```jupyter notebook --generate-config``` to generate a clean configuration file with all parameters commented out
# - modify `c.NotebookApp.iopub_data_rate_limit` and `c.NotebookApp.iopub_msg_rate_limit` to be some absurdly large numbers

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Tables

# %% {"slideshow": {"slide_type": "fragment"}}
import plotly.offline as py
import plotly.figure_factory as ff

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

table = ff.create_table(df)
py.iplot(table, filename='plotly\table1')

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Bar graphs

# %% {"slideshow": {"slide_type": "fragment"}}
import plotly.offline as py
from plotly.graph_objs import *
data = [Bar(x=df.School,
            y=df.Gap)]

py.iplot(data)

# %% {"slideshow": {"slide_type": "fragment"}}
trace_women = Bar(x=df.School,
                  y=df.Women,
                  name='Women',
                  marker=dict(color='#ffcdd2'))

trace_men = Bar(x=df.School,
                y=df.Men,
                name='Men',
                marker=dict(color='#A2D5F2'))

trace_gap = Bar(x=df.School,
                y=df.Gap,
                name='Gap',
                marker=dict(color='#59606D'))

data = [trace_women, trace_men, trace_gap]
layout = Layout(title="Average Earnings for Graduates",
                xaxis=dict(title='School'),
                yaxis=dict(title='Salary (in thousands)'))
fig = Figure(data=data, layout=layout)

py.iplot(fig)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Interactive slider

# %% {"slideshow": {"slide_type": "fragment"}}
data = [dict(
        visible = False,
        line=dict(color='00CED1', width=6),
        name = '𝜈 = '+str(step),
        x = np.arange(0,10,0.01),
        y = np.sin(step*np.arange(0,10,0.01))) for step in np.arange(0,5,0.1)]
data[10]['visible'] = True

steps = []
for i in range(len(data)):
    step = dict(
        method = 'restyle',
        args = ['visible', [False] * len(data)],
    )
    step['args'][1][i] = True # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active = 10,
    currentvalue = {"prefix": "Frequency: "},
    pad = {"t": 50},
    steps = steps
)]

layout = dict(sliders=sliders)
fig = dict(data=data, layout=layout)

py.iplot(fig)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Interactive 3D Plots

# %% {"slideshow": {"slide_type": "fragment"}}
s = np.linspace(0, 2 * np.pi, 240)
t = np.linspace(0, np.pi, 240)
tGrid, sGrid = np.meshgrid(s, t)

r = 2 + np.sin(7 * sGrid + 5 * tGrid)  # r = 2 + sin(7s+5t)
x = r * np.cos(sGrid) * np.sin(tGrid)  # x = r*cos(s)*sin(t)
y = r * np.sin(sGrid) * np.sin(tGrid)  # y = r*sin(s)*sin(t)
z = r * np.cos(tGrid)                  # z = r*cos(t)

surface = Surface(x=x, y=y, z=z)
data = Data([surface])

layout = Layout(
    title='Parametric Plot',
    scene=Scene(
        xaxis=XAxis(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=YAxis(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=ZAxis(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    )
)

fig = Figure(data=data, layout=layout)
py.iplot(fig)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Other plot aesthetics

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Wes Anderson color palettes
# You can generate these with the `wes` Python package. 
# <br><br>
# That said, installation can be a little annoying, since you will often get an error for missing the `colors.json` file. If you get that error, simply download the [tarball of the latest version of the package](https://pypi.python.org/pypi/wes/0.1.5), extract `colors.json` and place it in the appropriate location (i.e., where the error tells you it cannot be found).

# %% {"slideshow": {"slide_type": "fragment"}}
import wes
wes.available(show=True)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# And set the palette with the following code:

# %% {"slideshow": {"slide_type": "fragment"}}
wes.set_palette('Darjeeling')

for i in range(10):
    plt.plot(range(100), np.random.normal(i, 1, 100))

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Debugging in Jupyter Notebooks
# Use `set_trace()` where you want the debugger to start.<br>
# 'n' moves onto the next line<br>
# 'c' continues execution of the script

# %% {"collapsed": true, "slideshow": {"slide_type": "subslide"}}
from IPython.core.debugger import set_trace

def increment_value(a):
    a += 1
    set_trace()
    print(a)

increment_value(3)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Other Python tricks

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Get a function's source code

# %% {"scrolled": true, "slideshow": {"slide_type": "fragment"}}
import inspect
import numpy as np

print(inspect.getsource(np))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Find where a function lives

# %% {"slideshow": {"slide_type": "fragment"}}
inspect.getfile(np)

# %% [markdown]
# ## Memoization

# %% [markdown]
# Memoization can make recursive functions run faster.

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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Miscellany
# If you want to start digging deeper into Python, you can [learn some cool things here](https://www.youtube.com/watch?v=7lmCu8wz8ro&index=2&list=PLl_RiCpxqWcAKgcznY3IxZ3ZMRFTvp2Z2&t=3638s), and [here](https://youtu.be/OSGv2VnC0go), and [here](http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html). 

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# That said, here is my favorite random snippet of python code ever. You can swap variable values without needing any temporary variables via **tuple unpacking**. 

# %% {"slideshow": {"slide_type": "fragment"}}
a = "A"
b = "B"

# Swap!
a, b = b, a 

print("a = " + a)
print("b = " + b)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# And extended unpacking is interesting to wrap your head around (Python 3 only).

# %% {"slideshow": {"slide_type": "fragment"}}
a, *b, c = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print(c)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# List comprehensions are also extremely useful, allowing you to program almost as if you were writing a sentence in English.

# %% {"slideshow": {"slide_type": "fragment"}}
# get sum of squares of numbers taken from the range 1 to 10
sum(i**2 for i in range(11))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Zipping lists is another one of my favorite features.

# %% {"slideshow": {"slide_type": "fragment"}}
a = ['a', 'b', 'c']
b = [1, 2, 3]

c = zip(a, b)
clist = list(c)
print(clist) # need to cast into a list because a zip object is a generator

# %% [markdown]
# And you can always unzip a list, too.

# %%
unzipped = zip(*clist)
print(list(unzipped))

# %% [markdown]
# Since functions are first class citizens in Python, you can even assign them to dictionaries! This means you can [make a dictionary of _functions_](https://code.activestate.com/recipes/65126-dictionary-of-methodsfunctions/) which you can call later down the line. This opens up a lot of possibilities — use your imagination!

# %%
def function1():
    print("called function 1")

def function2():
    print("called function 2")

def function3():
    print("called function 3")

tokenDict = {"cat":function1, "dog":function2, "bear":function3}

# simulate, say, lines read from a file
lines = ["cat", "bear", "cat", "dog"]

for line in lines:
    # lookup the function to call for each line
    functionToCall = tokenDict[line]

    # and call it
    functionToCall()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Run R code
# <br>
# Note that this requires running from a Python 3 instance of Jupyter (in my case, at least).

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Example Python to R pipeline

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# First, make some example data in Python.

# %% {"collapsed": true, "slideshow": {"slide_type": "fragment"}}
import pandas as pd
df = pd.DataFrame({'Letter': ['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],
                   'X': [4, 3, 5, 2, 1, 7, 7, 5, 9],
                   'Y': [0, 4, 3, 6, 7, 10, 11, 9, 13],
                   'Z': [1, 2, 3, 1, 2, 3, 1, 2, 3]})

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Load extension allowing one to run R code from within a Python notebook.

# %% {"collapsed": true, "slideshow": {"slide_type": "fragment"}}
# %load_ext rpy2.ipython

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Do stuff in R with cell or line magics. "-i" imports to R, "-o" outputs from R back to Python.

# %% {"collapsed": true, "slideshow": {"slide_type": "fragment"}, "language": "R"}
# install.packages("ggplot2", dep=TRUE)
# install.packages("tidyr", dep=TRUE)
# install.packages("dplyr", dep=TRUE)

# %% {"slideshow": {"slide_type": "fragment"}, "magic_args": "-i df", "language": "R"}
# library("ggplot2")
# ggplot(data = df) + geom_point(aes(x = X, y = Y, color = Letter, size = Z))

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Run MATLAB code

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## MATLAB for Jupyter installation

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
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

# %% {"slideshow": {"slide_type": "fragment"}}
# %load_ext pymatbridge

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Let's try transposing an array from Python in MATLAB, then feeding it back into Python.
# <br><br>
# First, define an array.

# %% {"slideshow": {"slide_type": "fragment"}}
a = [
    [1, 2],
    [3, 4],
    [5, 6]
]
a

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Now transpose it easily in MATLAB!

# %% {"slideshow": {"slide_type": "fragment"}}
# %%matlab -i a -o a
a = a'

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Finally, check that Python has the correct value of `a`.

# %% {"slideshow": {"slide_type": "fragment"}}
a

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Here's an example of a MATLAB plot.

# %% {"slideshow": {"slide_type": "fragment"}}
# %%matlab
b = linspace(0.01,6*pi,100);
plot(sin(b))
grid on
hold on
plot(cos(b),'r')

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Exit MATLAB when done.

# %% {"slideshow": {"slide_type": "fragment"}}
# %unload_ext pymatbridge

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Run Javascript code
# <br>
# Note that Javascript executes as the notebook is opened, even if it's been exported as HTML!

# %% {"slideshow": {"slide_type": "subslide"}, "language": "javascript"}
# console.log('hey!')

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # [Interesting Example Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)
