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

# Intro to data analysis with pandas


# In-depth pandas tutorial
[Giant pandas tutorial](https://www.youtube.com/watch?v=oGzU688xCUs) and [attendant notes](https://github.com/chendaniely/scipy-2017-tutorial-pandas) available at the links.


# Imports
Allow plots in the notebook itself, and enable some helpful functions

```python
%reset -f
%matplotlib inline
%config InlineBackend.figure_format = 'retina' # High-res graphs (rendered irrelevant by svg option below)
%config InlineBackend.print_figure_kwargs = {'bbox_inches':'tight'} # No extra white space
%config InlineBackend.figure_format = 'svg' # 'png' is default

import warnings
warnings.filterwarnings('ignore') # Because we are adults
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

```python
data = sns.load_dataset("tips")
data.head()  # show first n entries (default is 5)
```

# Data exploration


## Histograms

```python
data["tip"].hist(by=data["sex"], sharex=True, sharey=True)
sns.despine()  # Remove top and right side of box

plt.show()  # Somewhat redundant in this context, but suppresses annoying text output.
```

## Overlaid histograms

```python
grouped_by_sex = data.groupby("sex")

# You can also add several arguments below like bins=20, or normed=True
figure, axes = grouped_by_sex["tip"].plot(
    kind="hist", normed=False, alpha=0.5, legend=True
)

# Re-label legend entries, move legend to right-middle
axes.legend(["Men", "Women"], loc=(0.75, 0.5))

sns.despine()
plt.show()
```

## Descriptive statistics

```python
grouped_by_sex["tip"].describe()
```

## Subsetting data
Let's get the tips given on Sunday at dinner time only.

```python
sunday_dinner_tips = data.tip[(data.day == "Sun") & (data.time == "Dinner")]
```

## Data processing


### Add new column
Add a new column showing the percentage of the total bill tipped using a lambda expression. Naturally, you can also accomplish this by defining a named function.

```python
data["tip_percentage"] = data.apply(
    lambda row: row["tip"] / row["total_bill"] * 100, axis=1
)
data.head()
```

## Deleting columns
Delete that new tip percentage column.

```python
del data["tip_percentage"]
data.head()
```

# Inferential Statistics
Examples of inferential statistics using statsmodels. Note that there are some recent and annoying breaking changes between pandas and numpy when dealing with pandas's "categorical" data type.


## ANOVA
Perform an ANOVA using syntax akin to that of R.


First, figure out which columns have the annoying "categorical" data type.

```python
data.dtypes
```

Second, convert those to strings (will show as "object", which numpy can actually understand).

```python
categories = ["sex", "smoker", "day", "time"]

for category in categories:
    data[category] = data[category].astype(str)

data.dtypes
```

Now run the ANOVA.

```python
import statsmodels.api as sm
from statsmodels.formula.api import ols

model = "tip ~ day * smoker"
lm = ols(model, data=data).fit()
# lm.summary() # to show regression results
table = sm.stats.anova_lm(lm, typ=2)

display(table)
```

## Table aesthetics
Make the table prettier and more intelligible.

```python
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
```

## T-tests

```python
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
```

## Place statistics in text with Markdown

```python
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
```

And in plain markdown:
_t_({{n-2}})={{format(t, '.2f').lstrip('0')}}, *p*{{inequality_symbol}}{{format(p, '.3f').lstrip('0')}}, *d*={{format(d, '.3f').lstrip('0')}}

<div class="alert alert-block alert-info">
Note that you can copy paste such outputs directly into Word with no loss of formatting!
</div>


## Repeated Measures ANOVA
[See example here.](https://www.marsja.se/repeated-measures-anova-in-python-using-statsmodels/)

```python
import pandas as pd
import numpy as np
import statsmodels
from statsmodels.stats.anova import AnovaRM
statsmodels.__version__
```

```python
N = 20
P = [1, 2]

values = [998, 511]

sub_id = [i + 1 for i in range(N)] * len(P)
mus = np.concatenate([np.repeat(value, N) for value in values]).tolist()
rt = np.random.normal(mus, scale=112.0, size=N * len(P)).tolist()
iv = np.concatenate([np.array([p] * N) for p in P]).tolist()

df = pd.DataFrame({"id": sub_id, "rt": rt, "iv": iv})
```

```python
aovrm = AnovaRM(df, depvar="rt", subject="id", within=["iv"])
fit = aovrm.fit()
fit.summary()
```
