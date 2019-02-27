# -*- coding: utf-8 -*-
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
#   rise:
#     theme: moon
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
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
# # Imports

# %%
# %reset -f
# %matplotlib inline 
# %config InlineBackend.figure_format = "retina" # High-res graphs (rendered irrelevant by svg option below)
# %config InlineBackend.print_figure_kwargs = {"bbox_inches": "tight"} # No extra white space
# %config InlineBackend.figure_format = "svg" # "png" is default
 
import warnings
warnings.filterwarnings("ignore") # Because we are adults
from IPython.core.debugger import set_trace
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
 
# iPyPublish imports
# from ipypublish.scripts.ipynb_latex_setup import *
# from IPython.display import SVG, display, Markdown

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Matplotlib
# The bread and butter for plotting in Python. See [here](https://matplotlib.org/tutorials/index.html) and [Ben Deverett's excellent notebook](https://github.com/bensondaled/princetonpy/tree/master/20181204) for tutorials.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## xkcd Style Plots

# %%
with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Monroe
    # http://xkcd.com/418/

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks([])
    plt.yticks([])
    ax.set_ylim([-30, 10])

    data = np.ones(100)
    data[70:] -= np.arange(30)

    plt.annotate(
        'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
        xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

    plt.plot(data)

    plt.xlabel('time')
    plt.ylabel('my overall health')
    fig.text(
        0.5, 0.05,
        '"Stove Ownership" from xkcd by Randall Monroe',
        ha='center')

# %% {"slideshow": {"slide_type": "subslide"}}
with plt.xkcd():
    # Based on "The Data So Far" from XKCD by Randall Monroe
    # http://xkcd.com/373/

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.bar([0, 1], [0, 100], 0.25)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([0, 1])
    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([0, 110])
    ax.set_xticklabels(['CONFIRMED BY\nEXPERIMENT', 'REFUTED BY\nEXPERIMENT'])
    plt.yticks([])

    plt.title("CLAIMS OF SUPERNATURAL POWERS")

    fig.text(
        0.5, -0.05,
        '"The Data So Far" from xkcd by Randall Monroe',
        ha='center')

plt.show()

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "toc-hr-collapsed": false}
# # Seaborn
# Wrapper around Matplotlib that makes plotting attractive figures easier.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Changing color palette

# %%
pal = sns.color_palette("husl", 8)  # optionally set number of colors
sns.set_palette(pal)
sns.palplot(sns.color_palette())

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Default Seaborn color palette

# %%
sns.set_palette("tab10")
sns.palplot(sns.color_palette())

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Defining custom color palette

# %%
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.set_palette(flatui)
sns.palplot(sns.color_palette())

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Wes Anderson color palettes
# You can generate these with the wes Python package. 
#
# That said, installation can be a little annoying, since you will often get an error for missing the colors.json file. If you get that error, simply [download the tarball of the latest version of the package](https://pypi.org/project/wes/0.1.5/), extract colors.json and place it in the appropriate location (i.e., where the error tells you it cannot be found).

# %%
import wes
wes.available(show=True)
# wes.set_palette('Darjeeling')

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Line plot

# %%
sns.set(style="ticks")  # overwrites color palette

# Load the example dataset for Anscombe's quartet
anscombe = sns.load_dataset("anscombe")

# And of course, you can combine it with xkcd style if you want
with plt.xkcd():
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
        height=4,  # palette=pal,
        scatter_kws={"s": 50, "alpha": 1},
    )

    # Change axis labels
    ax.set(xlabel="X", ylabel="Y");

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Bar chart
# Defaults to showing the 95% confidence interval.

# %%
tips = sns.load_dataset("tips")
ax = sns.barplot(x="day", y="total_bill", data=tips, capsize=0.1)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Subplots -- Violin plot with overlaid beeswarm plot

# %%
wes.set_palette("Darjeeling")  # change the color scheme

fig, ax = plt.subplots()

# Output to the size of A4 paper
fig.set_size_inches(11.7, 8.27)

# Overlay a swarmplot on top of a violinplot
ax = sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
ax = sns.swarmplot(x="day", y="total_bill", data=tips, color="white")
ax.set(xlabel="Day of the Week", ylabel="Total Bill in $");

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Factor plots (catplot)

# %%
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
barPlot = sns.catplot(
    x="day",
    y="total_bill",
    hue="sex",
    col="time",
    kind="bar",
    data=tips,
    height=5,
    aspect=1,
    legend=False,
);

beeswarmPlot = sns.catplot(
    x="day",
    y="total_bill",
    hue="sex",
    col="time",
    kind="swarm",
    dodge=True,
    data=tips,
    height=5,
    aspect=1,
    legend=False,
);

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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Layered histogram

# %%
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Bokeh
# Interactive visualization library leveraging JavaScript. [See here for a video tutorial](https://www.youtube.com/watch?v=9FlUFLmaWvY) and [here for a notebook with various visualizations](https://github.com/claresloggett/demo_visualisation_python/blob/master/Demo_Visualisation.ipynb), including some made with Bokeh.

# %%
from bokeh.plotting import figure, output_notebook, show

this_plot = figure(width=600, height=600)

this_plot.circle(x=tips["total_bill"], y=tips["tip"], size=10, alpha=0.7)
output_notebook()  # to output inline
show(this_plot)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## More interactive plot
# Let's plot a scatterplot of tip amount vs. total bill, separately for men and women.
#
# [See here for more information on styling Bokeh plots.](https://bokeh.pydata.org/en/latest/docs/user_guide/styling.html)

# %%
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Pivot table plots

# %%
from pivottablejs import pivot_ui
pivot_ui(tips)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Dash/Plotly
# [Dash/Plotly](https://plot.ly/products/dash/) is another package for producing really nice and interactive graphs, but it requires signing up for an account to initialize it. After initialization you can use it online by default (which means all of your graphs get saved to the cloud for everyone to see forever) or you can use it offline (as demoed below). Examples taken or modified from [here](https://plot.ly/python/ipython-notebook-tutorial/).  
#
# I'm not familiar with the new Dash API that's been recently introduced, nor have I really explored using Plotly. I've been able to get everything that I need done in Matplotlib/Seaborn, so understand that the code snippets below may no longer work with recent versions of the Plotly package (which seems like a different thing to Dash).

# %% [markdown] {"slideshow": {"slide_type": "skip"}}
# ## Troubleshooting setup
# When I first tried using plotly I sometimes got `IOPub data rate exceeded` errors. Here's how you fix that:
#
# - run `jupyter notebook --generate-config` to generate a clean configuration file with all parameters commented out
# - modify `c.NotebookApp.iopub_data_rate_limit` and `c.NotebookApp.iopub_msg_rate_limit` to be some absurdly large numbers

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Simple line graph

# %%
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Tables

# %%
import plotly.offline as py
import plotly.figure_factory as ff

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

table = ff.create_table(df)
py.iplot(table, filename='plotly\table1')

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Bar graphs

# %%
import plotly.offline as py
from plotly.graph_objs import *
data = [Bar(x=df.School,
            y=df.Gap)]

py.iplot(data)

# %% {"slideshow": {"slide_type": "subslide"}}
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Interactive Slider

# %% {"lines_to_next_cell": 2}
data = [
    dict(
        visible=False,
        line=dict(color="#00CED1", width=6),
        name="𝜈 = " + str(step),
        x=np.arange(0, 10, 0.01),
        y=np.sin(step * np.arange(0, 10, 0.01)),
    )
    for step in np.arange(0, 5, 0.1)
]
data[10]["visible"] = True

steps = []
for i in range(len(data)):
    step = dict(method="restyle", args=["visible", [False] * len(data)])
    step["args"][1][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [
    dict(active=10, currentvalue={"prefix": "Frequency: "}, pad={"t": 50}, steps=steps)
]

layout = dict(sliders=sliders)
fig = dict(data=data, layout=layout)

py.iplot(fig)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Interactive 3D Plot

# %% {"lines_to_next_cell": 2}
s = np.linspace(0, 2 * np.pi, 240)
t = np.linspace(0, np.pi, 240)
tGrid, sGrid = np.meshgrid(s, t)

r = 2 + np.sin(7 * sGrid + 5 * tGrid)  # r = 2 + sin(7s+5t)
x = r * np.cos(sGrid) * np.sin(tGrid)  # x = r*cos(s)*sin(t)
y = r * np.sin(sGrid) * np.sin(tGrid)  # y = r*sin(s)*sin(t)
z = r * np.cos(tGrid)  # z = r*cos(t)

surface = Surface(x=x, y=y, z=z)
data = Data([surface])

layout = Layout(
    title="Parametric Plot",
    scene=Scene(
        xaxis=XAxis(
            gridcolor="rgb(255, 255, 255)",
            zerolinecolor="rgb(255, 255, 255)",
            showbackground=True,
            backgroundcolor="rgb(230, 230,230)",
        ),
        yaxis=YAxis(
            gridcolor="rgb(255, 255, 255)",
            zerolinecolor="rgb(255, 255, 255)",
            showbackground=True,
            backgroundcolor="rgb(230, 230,230)",
        ),
        zaxis=ZAxis(
            gridcolor="rgb(255, 255, 255)",
            zerolinecolor="rgb(255, 255, 255)",
            showbackground=True,
            backgroundcolor="rgb(230, 230,230)",
        ),
    ),
)

fig = Figure(data=data, layout=layout)
py.iplot(fig)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # ggplot (plotnine)
# If you have a background in R, you can use the plotnine library as a plug-in replacement for ggplot in Python. It has the same API you're familiar with. Combine with [dfply](https://github.com/kieferk/dfply) and pandas for a very good implementation of the tidyverse in Python.

# %% {"lines_to_next_cell": 2}
from plotnine import *

iris = sns.load_dataset("iris")

(
    ggplot(iris)
    + aes(x="sepal_length", y="petal_length", colour="species")
    + geom_point()
)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # PyViz (holoviews)
#
# [See here for tutorial.](http://pyviz.org/tutorial/scipy18)

# %% [markdown]
# ## Scatterplot matrix

# %%
import holoviews as hv
import hvplot
import hvplot.pandas
hv.extension("bokeh") # use bokeh backend

iris = sns.load_dataset("iris")
hvplot.scatter_matrix(iris, c='species')

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Time series

# %%
# Get data
diseases = pd.read_csv("data/diseases.csv.gz")
diseases.head()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Static plot with pandas

# %%
measles_by_year = diseases[["Year","measles"]].groupby("Year").aggregate(np.sum)
measles_by_year.plot();

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Same thing with dfply

# %% {"scrolled": false}
from dfply import *
measles_by_year = (
    diseases
    >> select(X.Year, X.measles)
    >> group_by(X.Year)
    >> summarize_each([np.sum], X.measles)
)
measles_by_year.set_index("Year", inplace=True)
measles_by_year.plot();

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Interactive plot with holoviews

# %%
measles_by_year.hvplot()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Annotating figure
# Show when measles vaccine was introduced with a vertical line.

# %% {"slideshow": {"slide_type": "-"}}
vline = hv.VLine(1963).opts(color='black')
g = measles_by_year.hvplot() * vline * \
    hv.Text(1963, 27000, " Vaccine introduced", halign='left')
g

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Dropdown menus

# %%
measles_agg = diseases.groupby(['Year', 'State'])['measles'].sum()
measles_by_state = measles_agg.hvplot('Year', groupby='State', width=500, dynamic=False)

measles_by_state * vline

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "toc-hr-collapsed": false}
# # Altair

# %% [markdown]
# Declarative plotting library with a lot of useful chart types. Examples below are taken from [here](https://altair-viz.github.io/gallery/).

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Simple scatterplot with tooltips

# %%
from vega_datasets import data

# Enable notebook renderer once per session
# only necessary in jupyter notebook, not jupyter lab.
# alt.renderers.enable("notebook")

cars = data.cars()

alt.Chart(cars).mark_circle(size=60).encode(
    x="Miles_per_Gallon",
    y="Horsepower",
    color="Origin",
    tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
).interactive()

# %% [markdown]
# ## Interval selection

# %%
# Can choose just x, just y, or both as below for interval
interval = alt.selection_interval(encodings=["x", "y"])

chart = alt.Chart(cars).mark_circle(size=60).encode(
    x="Miles_per_Gallon",
    y="Horsepower",
    color=alt.condition(interval, "Origin", alt.value("lightgray")),
    tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
).properties(
    selection=interval
)

# %% [markdown]
# ## Placing figures side by side with `|`
# The figures will be linked.

# %%
concatenated_chart = chart | chart.encode(x="Acceleration")

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Scatterplot matrix

# %%
alt.Chart(cars).mark_circle().encode(
    alt.X(alt.repeat("column"), type="quantitative"),
    alt.Y(alt.repeat("row"), type="quantitative"),
    color="Origin:N",
).properties(width=150, height=150).repeat(
    row=["Horsepower", "Acceleration", "Miles_per_Gallon"],
    column=["Miles_per_Gallon", "Acceleration", "Horsepower"],
).interactive()

# %% [markdown]
# ## Exporting to HTML

# %%
concatenated_chart.save("concat.html")

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Conclusion

# %% [markdown] {"slideshow": {"slide_type": "-"}}
# As you can see, there is no shortage of powerful visualization options in Python. That said, I'm still partial to seaborn and matplotlib for making publication-quality static figures (but I'm very excited about the possibilities Altair brings to data exploration).

# %%
sns.pairplot(iris, hue="species");
