---
jupyter:
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
---

# Imports

```python
%reset -f
%matplotlib inline 
%config InlineBackend.figure_format = 'retina' # High-res graphs (rendered irrelevant by svg option below)
%config InlineBackend.print_figure_kwargs = {'bbox_inches':'tight'} # No extra white space
%config InlineBackend.figure_format = 'svg' # 'png' is default
 
import warnings
warnings.filterwarnings('ignore') # Because we are adults
from IPython.core.debugger import set_trace
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
 
# iPyPublish imports
# from ipypublish.scripts.ipynb_latex_setup import *
# from IPython.display import SVG, display, Markdown
```

# Matplotlib
The bread and butter for plotting in Python. See [here](https://matplotlib.org/tutorials/index.html) and [Ben Deverett's excellent notebook](https://github.com/bensondaled/princetonpy/tree/master/20181204) for tutorials.


# Seaborn
Wrapper around Matplotlib that makes plotting attractive figures easier.


## Changing color palette

```python
pal = sns.color_palette("husl", 8)  # optionally set number of colors
sns.set_palette(pal)
sns.palplot(sns.color_palette())
```

## Default Seaborn color palette

```python
sns.set_palette("tab10")
sns.palplot(sns.color_palette())
```

## Defining custom color palette

```python
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.set_palette(flatui)
sns.palplot(sns.color_palette())
```

## Wes Anderson color palettes
You can generate these with the wes Python package. 

That said, installation can be a little annoying, since you will often get an error for missing the colors.json file. If you get that error, simply [download the tarball of the latest version of the package](https://pypi.org/project/wes/0.1.5/), extract colors.json and place it in the appropriate location (i.e., where the error tells you it cannot be found).

```python
import wes
wes.available(show=True)
# wes.set_palette('Darjeeling')
```

## Line plot

```python
sns.set(style="ticks")  # overwrites color palette

# Load the example dataset for Anscombe's quartet
anscombe = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
# Semi-colon suppresses the non-graph output
ax = sns.lmplot(
    x="x",
    y="y",
    col="dataset",
    hue="dataset",
    data=anscombe,
    col_wrap=2,
    ci=None,
    size=4,  # palette=pal,
    scatter_kws={"s": 50, "alpha": 1},
)

# Change axis labels
ax.set(xlabel="X", ylabel="Y")
```

## Bar chart
Defaults to showing the 95% confidence interval.

```python
tips = sns.load_dataset("tips")
ax = sns.barplot(x="day", y="total_bill", data=tips, capsize=0.1)
```

## Subplots -- Violin plot with overlaid beeswarm plot

```python
sns.set_palette(flatui)  # change the color scheme

fig, ax = plt.subplots()

# Output to the size of A4 paper
fig.set_size_inches(11.7, 8.27)

# Overlay a swarmplot on top of a violinplot
ax = sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
ax = sns.swarmplot(x="day", y="total_bill", data=tips, color="white")
ax.set(xlabel="Day of the Week", ylabel="Total Bill in $")
```

## Factor plots 

```python
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
    thisPlot.axes[0][maxIndex].legend(
        bbox_to_anchor=(1.05, 1), loc=2, fontsize=fontSize, borderaxespad=0.0
    )
    legend = thisPlot.axes[0][maxIndex].get_legend()
    labels = legend.get_texts()
    for i, thisLabel in enumerate(labels):
        labels[i].set_text(legendEntries[i])


sns.set_palette("tab10")

# Make plots -- many of these arguments are optional
barPlot = sns.factorplot(
    x="day",
    y="total_bill",
    hue="sex",
    col="time",
    kind="bar",
    data=tips,
    size=5,
    aspect=1,
    legend=False,
)

beeswarmPlot = sns.factorplot(
    x="day",
    y="total_bill",
    hue="sex",
    col="time",
    kind="swarm",
    dodge=True,
    data=tips,
    size=5,
    aspect=1,
    legend=False,
)

# Format them nicely!
# Axis labels
xLabel = ""  # "Day"
yLabel = "Total Bill"
set_labels(barPlot, xLabel, yLabel, 20)
set_labels(beeswarmPlot, xLabel, yLabel, 20)

# Titles
title_list = ["Lunch", "Dinner"]
titles = [x.title() for x in title_list]  # ["Bimodal", "Normal", "Skewed"]
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
```

# Altair


Declarative plotting library with a lot of useful chart types. Examples below are taken from [here](https://altair-viz.github.io/gallery/).


## Simple scatterplot with tooltips

```python
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_circle(size=60).encode(
    x="Horsepower",
    y="Miles_per_Gallon",
    color="Origin",
    tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
).interactive()
```

## Scatterplot matrix

```python
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_circle().encode(
    alt.X(alt.repeat("column"), type="quantitative"),
    alt.Y(alt.repeat("row"), type="quantitative"),
    color="Origin:N",
).properties(width=150, height=150).repeat(
    row=["Horsepower", "Acceleration", "Miles_per_Gallon"],
    column=["Miles_per_Gallon", "Acceleration", "Horsepower"],
).interactive()
```

## Layered histogram

```python
import pandas as pd
import altair as alt
import numpy as np

np.random.seed(42)

# Generating Data
source = pd.DataFrame(
    {
        "Trial A": np.random.normal(0, 0.8, 1000),
        "Trial B": np.random.normal(-2, 1, 1000),
        "Trial C": np.random.normal(3, 2, 1000),
    }
)

# Tidying Data
source = pd.melt(
    source,
    id_vars=source.index.name,
    value_vars=source.columns,
    var_name="Experiment",
    value_name="Measurement",
)

alt.Chart(source).mark_area(opacity=0.3, interpolate="step").encode(
    alt.X("Measurement", bin=alt.Bin(maxbins=100)),
    alt.Y("count()", stack=None),
    alt.Color("Experiment", scale=alt.Scale(range=["#0000ff", "#008000", "#ff0000"])),
)
```

# Bokeh
Interactive visualization library leveraging JavaScript. [See here for a video tutorial](https://www.youtube.com/watch?v=9FlUFLmaWvY) and [here for a notebook with various visualizations](https://github.com/claresloggett/demo_visualisation_python/blob/master/Demo_Visualisation.ipynb), including some made with Bokeh.

```python
from bokeh.plotting import figure, output_notebook, show

this_plot = figure(width=600, height=600)

this_plot.circle(x=tips["total_bill"], y=tips["tip"], size=10, alpha=0.7)
output_notebook()  # to output inline
show(this_plot)
```

## More interactive plot
Let's plot a scatterplot of tip amount vs. total bill, separately for men and women.

[See here for more information on styling Bokeh plots.](https://bokeh.pydata.org/en/latest/docs/user_guide/styling.html)

```python
from bokeh.plotting import figure, output_notebook, show, ColumnDataSource
import bokeh.models.tools as tools

# Get relevant subsets of data
male_data = tips[tips["sex"] == "Male"]
female_data = tips[tips["sex"] == "Female"]

# Convert to format bokeh understands
source_male = ColumnDataSource(male_data)
source_female = ColumnDataSource(female_data)

# Set up figure
this_plot = figure(width=600, height=600)

this_plot.circle(
    source=source_male,
    x="total_bill",
    y="tip",
    color="teal",
    size=10,
    alpha=0.7,
    legend="Men",
)

this_plot.circle(
    source=source_female,
    x="total_bill",
    y="tip",
    color="darkorange",
    size=10,
    alpha=0.7,
    legend="Women",
)

# Set axis labels
this_plot.xaxis.axis_label = "Total Bill"
this_plot.yaxis.axis_label = "Tip Amount"

# Show information when hovering the mouse over datapoints
this_plot.add_tools(tools.HoverTool(tooltips=[("Day", "@day")]))  # @ chooses feature

# Hide all circles of a given category when clicked in legend
this_plot.legend.click_policy = "hide"

output_notebook()
show(this_plot)
```

# Pivot table plots

```python
from pivottablejs import pivot_ui
pivot_ui(tips)
```

# Dash/Plotly
[Dash/Plotly](https://plot.ly/products/dash/) is another package for producing really nice and interactive graphs, but it requires signing up for an account to initialize it. After initialization you can use it online by default (which means all of your graphs get saved to the cloud for everyone to see forever) or you can use it offline (as demoed below). Examples taken or modified from [here](https://plot.ly/python/ipython-notebook-tutorial/).  

I'm not familiar with the new Dash API that's been recently introduced, nor have I really explored using Plotly. I've been able to get everything that I need done in Matplotlib/Seaborn, so understand that the code snippets below may no longer work with recent versions of the Plotly package (which seems like a different thing to Dash).


## Troubleshooting setup
When I first tried using plotly I sometimes got `IOPub data rate exceeded` errors. Here's how you fix that:

- run `jupyter notebook --generate-config` to generate a clean configuration file with all parameters commented out
- modify `c.NotebookApp.iopub_data_rate_limit` and `c.NotebookApp.iopub_msg_rate_limit` to be some absurdly large numbers

```python
import plotly
# initialize with your credentials -- only need to do once ever in life, 
# not even once per notebook.
# plotly.tools.set_credentials_file(username='XXX', api_key='XXX') 
from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

plotly.offline.iplot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})
```

## Tables

```python
import plotly.offline as py
import plotly.figure_factory as ff

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

table = ff.create_table(df)
py.iplot(table, filename='plotly\table1')
```

## Bar graphs

```python
import plotly.offline as py
from plotly.graph_objs import *
data = [Bar(x=df.School,
            y=df.Gap)]

py.iplot(data)
```

```python
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
```

# Interactive Slider

```python
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
```

## Interactive 3D Plot

```python
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
```

```python

```
