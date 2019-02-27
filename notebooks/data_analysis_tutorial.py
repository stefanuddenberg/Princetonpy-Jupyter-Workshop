# ---
# jupyter:
#   celltoolbar: Slideshow
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
#     version: 3.7.2
#   toc:
#     nav_menu:
#       height: 162px
#       width: 246px
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
# # Intro to data analysis with pandas

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # In-depth pandas tutorial

# %% [markdown]
# [Giant pandas tutorial](https://www.youtube.com/watch?v=oGzU688xCUs) and [attendant notes](https://github.com/chendaniely/scipy-2017-tutorial-pandas) available at these links.

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Imports

# %% [markdown]
# Allow plots in the notebook itself, and enable some helpful functions

# %% {"slideshow": {"slide_type": "-"}}
# %reset -f
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina' # High-res graphs (rendered irrelevant by svg option below)
# %config InlineBackend.print_figure_kwargs = {'bbox_inches':'tight'} # No extra white space
# %config InlineBackend.figure_format = 'svg' # 'png' is default


import warnings
warnings.filterwarnings('ignore') # Because we are adults
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Data exploration

# %%
data = sns.load_dataset("tips")
data.head()  # show first n entries (default is 5)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Histograms

# %%
data["tip"].hist(by=data["sex"], sharex=True, sharey=True)
sns.despine()  # Remove top and right side of box

plt.show()  # Somewhat redundant in this context, but suppresses annoying text output.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Overlaid histograms

# %%
grouped_by_sex = data.groupby("sex")

# You can also add several arguments below like bins=20, or normed=True
figure, axes = grouped_by_sex["tip"].plot(
    kind="hist", normed=False, alpha=0.5, legend=True
)

# Re-label legend entries, move legend to right-middle
axes.legend(["Men", "Women"], loc=(0.75, 0.5))

sns.despine()
plt.show()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Descriptive statistics

# %%
grouped_by_sex["tip"].describe()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Subsetting data

# %% [markdown]
# Let's get the tips given on Sunday at dinner time only.

# %%
sunday_dinner_tips = data.tip[(data.day == "Sun") & (data.time == "Dinner")]

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Data processing

# %% [markdown] {"slideshow": {"slide_type": "-"}}
# ### Add new column

# %% [markdown]
# Add a new column showing the percentage of the total bill tipped using a lambda expression. Naturally, you can also accomplish this by defining a named function.

# %%
data["tip_percentage"] = data.apply(
    lambda row: row["tip"] / row["total_bill"] * 100, axis=1
)
data.head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Deleting columns

# %% [markdown]
# Delete that new tip percentage column.

# %%
del data["tip_percentage"]
data.head()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Inferential Statistics

# %% [markdown]
# Examples of inferential statistics using statsmodels. Note that there are some recent and annoying breaking changes between pandas and numpy when dealing with pandas's "categorical" data type.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## ANOVA

# %% [markdown]
# Perform an ANOVA using syntax akin to that of R. Because pandas recently changed how it represents categorical data, this requires a tiny bit of preprocessing.

# %% [markdown]
# ### ANOVA preprocessing
# First, figure out which columns have the annoying "categorical" data type.

# %%
data.dtypes

# %%
data.dtypes

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Second, convert those to strings (will show as "object", which numpy can actually understand).

# %%
categories = ["sex", "smoker", "day", "time"]

for category in categories:
    data[category] = data[category].astype(str)

data.dtypes

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Now run the ANOVA.

# %%
import statsmodels.api as sm
from statsmodels.formula.api import ols

model = "tip ~ day * smoker"
lm = ols(model, data=data).fit()
# lm.summary() # to show regression results
table = sm.stats.anova_lm(lm, typ=2)

display(table)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Table aesthetics

# %% [markdown]
# Make the table prettier and more intelligible.

# %%
def color_significant_green(val, alpha=0.05):
    if val < alpha:
        color = "green"
    else:
        color = "black"
    return "color: %s" % color


def bold_significant(val, alpha=0.05):
    if val < alpha:
        font_weight = "bold"
    else:
        font_weight = "normal"
    return "font-weight: %s" % font_weight


(
    table.style.applymap(color_significant_green, alpha=0.05, subset=["PR(>F)"])
    .applymap(bold_significant, alpha=0.05, subset=["PR(>F)"])
    .format("{:.3f}", subset=["sum_sq", "F", "PR(>F)"])  # show only 3 decimal places
)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## T-tests

# %%
from numpy import sqrt
from scipy.stats import ttest_ind

def cohens_d(t, n):
    return 2 * t / sqrt(n - 2)


# Set up empty results table
columns = ["n", "t", "p", "d"]
index = []
results = pd.DataFrame(index=index, columns=columns)

# Get data for t-test
male_tips = data[data["sex"] == "Male"]["tip"]
female_tips = data[data["sex"] == "Female"]["tip"]

# Perform t-test and surrounding calculations
n = male_tips.count() + female_tips.count()
df = n - 2
t, p = ttest_ind(male_tips, female_tips)
d = cohens_d(t, n)

# Add data to table
comparison = "Male vs. Female"
results.loc[comparison] = [n, t, p, d]

# Output pretty table
(
    results.style.applymap(color_significant_green, subset=["p"])
    .applymap(bold_significant, subset=["p"])
    .format("{:.3f}", subset=["t", "p", "d"])
)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Place statistics in text with Markdown

# %%
from IPython.display import Markdown

inequality_symbol = "="


def report_t_test(df, t, p, d, alpha=0.001):
    if p < alpha:
        p = 0.001
        inequality_symbol = "<"
    else:
        inequality_symbol = "="

    T = format(t, ".2f").lstrip("0")  # 2 decimal places, no leading 0
    P = format(p, ".3f").lstrip("0")
    D = format(d, ".3f").lstrip("0")
    DF = format(df, "d")  # integer

    output = f"*t*({DF})={T}, _p_{inequality_symbol}{P}, *d*={D}"
    display(Markdown(output))


report_t_test(df, t, p, d)

# %% [markdown] {"slideshow": {"slide_type": "-"}, "variables": {"format(d, '.3f').lstrip('0')": ".178", "format(p, '.3f').lstrip('0')": ".166", "format(t, '.2f').lstrip('0')": "1.39", "inequality</em>symbol": "<p><strong>SyntaxError</strong>: invalid syntax (<ipython-input-71-c4d8463e4db3>, line 1)</p>\n", "n-2": "242"}}
# And in plain markdown:
# _t_({{n-2}})={{format(t, '.2f').lstrip('0')}}, *p*{{inequality_symbol}}{{format(p, '.3f').lstrip('0')}}, *d*={{format(d, '.3f').lstrip('0')}}
#
# <div class="alert alert-block alert-info">
# Note that you can copy paste such outputs directly into Word with no loss of formatting!
# </div>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Repeated Measures ANOVA

# %% [markdown]
# [See example here.](https://www.marsja.se/repeated-measures-anova-in-python-using-statsmodels/)

# %%
import pandas as pd
import numpy as np
import statsmodels
from statsmodels.stats.anova import AnovaRM
statsmodels.__version__

# %% [markdown]
# Generate dummy data.

# %% {"slideshow": {"slide_type": "-"}}
N = 20
P = [1, 2]

values = [998, 511]

sub_id = [i + 1 for i in range(N)] * len(P)
mus = np.concatenate([np.repeat(value, N) for value in values]).tolist()
rt = np.random.normal(mus, scale=112.0, size=N * len(P)).tolist()
iv = np.concatenate([np.array([p] * N) for p in P]).tolist()

df = pd.DataFrame({"id": sub_id, "rt": rt, "iv": iv})

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Do the repeated measures ANOVA.

# %%
aovrm = AnovaRM(df, depvar="rt", subject="id", within=["iv"])
fit = aovrm.fit()
fit.summary()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # dfply

# %% [markdown]
# For those of you who are familiar with R and the tidyverse, the [dfply package](https://github.com/kieferk/dfply) allows you to have dplyr-like piping in Python. The pipe operator for this package is `>>`, while the result of each computation step is given by `X`. `>>=` is used for in-place assignment. All the documentation is available at the link; I'm just going to go over some useful basics here.

# %%
from dfply import *

diamonds >> head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Selection

# %% [markdown]
# Select two of the columns using `X` to represent the piped data frame.

# %%
diamonds >> select(X.cut, X.carat) >> head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Alternatively, you can use an array of field names.

# %%
diamonds >> select(["cut", "carat"]) >> head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Or we can refer to the columns by their numerical index.

# %%
diamonds >> select(1, 0) >> head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Dropping

# %% [markdown]
# Works the same way as `select`.

# %%
# drop cut (1), price, x and y
diamonds >> drop(1, X.price, ["x", "y"]) >> head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Inverse selection

# %% [markdown]
# What if you want all the columns _except_ for some selection? Use the `~` operator. Only works with `X`-type selection.

# %%
# Select all columns except for carat, cut, and price
diamonds >> select(~X.carat, ~X.cut, ~X.price) >> head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Filtering

# %% [markdown]
# Filtering rows with logical criteria is done with either `mask` or `filter_by`.

# %%
diamonds >> mask(X.cut == "Ideal") >> head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# As with all things Python, multi-line statements can be placed between parentheses.

# %%
(
    diamonds
    >> filter_by(X.cut == "Ideal", X.color == "E", X.table < 55, X.price < 500)
    >> head()
)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Pulling

# %% [markdown]
# Retrieves a column as a pandas series, if you care about a particular column at the end of your pipeline.

# %%
(
    diamonds
    >> filter_by(X.cut == "Ideal", X.color == "E", X.table < 55, X.price < 500)
    >> pull("carat")
)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Sorting

# %% [markdown]
# Use `arrange`, which is a wrapper for `.sort_values` in pandas.

# %%
diamonds >> arrange(X.table, ascending=False) >> head(5)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Can sort by multiple values with array notation.

# %%
diamonds >> arrange(["color", "table"], ascending=False) >> head()

# %% {"slideshow": {"slide_type": "-"}}
(
    diamonds
    >> group_by(X.cut)
    >> arrange(X.price)    
    >> head(3)
    >> ungroup()
    >> mask(X.carat < 0.23)    
)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Creating new columns

# %% [markdown]
# Use `mutate()` to compute new columns.

# %%
diamonds >> mutate(x_plus_y=X.x + X.y) >> select(columns_from('x')) >> head(3)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Remember the `tips` data from earlier and how we made a `tip_percentage` column? This is much easier with dfply than native pandas.

# %%
tips = sns.load_dataset("tips")
tips >>= mutate(tip_percentage=X.tip / X.total_bill * 100)
tips.head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# `transmute()` to mutate and select variables.

# %%
diamonds >> transmute(x_plus_y=X.x + X.y, y_div_z=(X.y / X.z)) >> head(3)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Grouping

# %%
(
    diamonds
    >> group_by(X.cut)
    >> mutate(price_lead=lead(X.price), price_lag=lag(X.price))
    >> head(2) # select 2 of each cut, since grouped
    >> select(X.cut, X.price, X.price_lead, X.price_lag)
)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Summarizing

# %%
(
    diamonds
    >> group_by(X.cut)
    >> summarize(price_mean=X.price.mean(), price_std=X.price.std())
)

# %% {"slideshow": {"slide_type": "skip"}}
(
    diamonds
    >> group_by(X.cut, X.color)
    >> summarize(price_mean=X.price.mean(), price_std=X.price.std())    
)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Summarizing multiple columns with `summarize_each(function_list, *columns)`; can use your favorite indexing style for columns.

# %%
diamonds >> group_by(X.cut) >> summarize_each([np.mean, np.var], X.price, "depth", 5)
