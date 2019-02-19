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
    version: 3.6.7
---

This is a `bqplot` recreation of Mike Bostock's [Wealth of Nations](https://bost.ocks.org/mike/nations/). This was also done by [Gapminder](http://www.gapminder.org/world/#$majorMode=chart$is;shi=t;ly=2003;lb=f;il=t;fs=11;al=30;stl=t;st=t;nsl=t;se=t$wst;tts=C$ts;sp=5.59290322580644;ti=2013$zpv;v=0$inc_x;mmid=XCOORDS;iid=phAwcNAVuyj1jiMAkmq1iMg;by=ind$inc_y;mmid=YCOORDS;iid=phAwcNAVuyj2tPLxKvvnNPA;by=ind$inc_s;uniValue=8.21;iid=phAwcNAVuyj0XOoBL_n5tAQ;by=ind$inc_c;uniValue=255;gid=CATID0;by=grp$map_x;scale=log;dataMin=194;dataMax=96846$map_y;scale=lin;dataMin=23;dataMax=86$map_s;sma=49;smi=2.65$cd;bd=0$inds=;modified=60). It is originally based on a TED Talk by [Hans Rosling](http://www.ted.com/talks/hans_rosling_shows_the_best_stats_you_ve_ever_seen).

```python
%reset -f
%matplotlib inline
%config InlineBackend.figure_format = 'retina' # High-res graphs
%config InlineBackend.print_figure_kwargs = {'bbox_inches':'tight'} # No extra white space
%config InlineBackend.figure_format = 'svg' # 'png' is default

import pandas as pd
import numpy as np
import os

from bqplot import (
    LogScale, LinearScale, OrdinalColorScale, ColorAxis,
    Axis, Scatter, Lines, CATEGORY10, Label, Figure, Tooltip
)

from ipywidgets import HBox, VBox, IntSlider, Play, jslink
```

```python
initial_year = 1800
```

#### Cleaning and Formatting JSON Data

```python
data = pd.read_json(os.path.abspath("data/nations.json"))
```

```python
def clean_data(data):
    for column in ['income', 'lifeExpectancy', 'population']:
        data = data.drop(data[data[column].apply(len) <= 4].index)
    return data

def extrap_interp(data):
    data = np.array(data)
    x_range = np.arange(1800, 2009, 1.)
    y_range = np.interp(x_range, data[:, 0], data[:, 1])
    return y_range

def extrap_data(data):
    for column in ['income', 'lifeExpectancy', 'population']:
        data[column] = data[column].apply(extrap_interp)
    return data
```

```python
data = clean_data(data)
data = extrap_data(data)
```

```python
income_min, income_max = np.min(data['income'].apply(np.min)), np.max(data['income'].apply(np.max))
life_exp_min, life_exp_max = np.min(data['lifeExpectancy'].apply(np.min)), np.max(data['lifeExpectancy'].apply(np.max))
pop_min, pop_max = np.min(data['population'].apply(np.min)), np.max(data['population'].apply(np.max))
```

```python
def get_data(year):
    year_index = year - 1800
    income = data['income'].apply(lambda x: x[year_index])
    life_exp = data['lifeExpectancy'].apply(lambda x: x[year_index])
    pop =  data['population'].apply(lambda x: x[year_index])
    return income, life_exp, pop
```

#### Creating the Tooltip to display the required fields

`bqplot`'s native `Tooltip` allows us to simply display the data fields we require on a mouse-interaction.

```python
tt = Tooltip(fields=['name', 'x', 'y'], labels=['Country Name', 'Income per Capita', 'Life Expectancy'])
```

#### Creating the Label to display the year

Staying true to the `d3` recreation of the talk, we place a `Label` widget in the bottom-right of the `Figure` (it inherits the `Figure` co-ordinates when no scale is passed to it). With `enable_move` set to `True`, the `Label` can be dragged around. 

```python
year_label = Label(x=[0.75], y=[0.10], default_size=46, font_weight='bolder', colors=['orange'],
                   text=[str(initial_year)], enable_move=True)
```

#### Defining Axes and Scales

The inherent skewness of the income data favors the use of a `LogScale`. Also, since the color coding by regions does not follow an ordering, we use the `OrdinalColorScale`.

```python
x_sc = LogScale(min=income_min, max=income_max)
y_sc = LinearScale(min=life_exp_min, max=life_exp_max)
c_sc = OrdinalColorScale(domain=data['region'].unique().tolist(), colors=CATEGORY10[:6])
size_sc = LinearScale(min=pop_min, max=pop_max)
```

```python
ax_y = Axis(label='Life Expectancy', scale=y_sc, orientation='vertical', side='left', grid_lines='solid')
ax_x = Axis(label='Income per Capita', scale=x_sc, grid_lines='solid')
```

#### Creating the Scatter Mark with the appropriate size and color parameters passed

To generate the appropriate graph, we need to pass the population of the country to the `size` attribute and its region to the `color` attribute.

```python
# Start with the first year's data
cap_income, life_exp, pop = get_data(initial_year)
```

```python
wealth_scat = Scatter(x=cap_income, y=life_exp, color=data['region'], size=pop,
                      names=data['name'], display_names=False,
                      scales={'x': x_sc, 'y': y_sc, 'color': c_sc, 'size': size_sc},
                      default_size=4112, tooltip=tt, animate=True, stroke='Black',
                      unhovered_style={'opacity': 0.5})
```

```python
nation_line = Lines(x=data['income'][0], y=data['lifeExpectancy'][0], colors=['Gray'],
                       scales={'x': x_sc, 'y': y_sc}, visible=False)
```

#### Creating the Figure

```python
time_interval = 10
```

```python
fig = Figure(marks=[wealth_scat, year_label, nation_line], axes=[ax_x, ax_y],
             title='Health and Wealth of Nations', animation_duration=time_interval)
```

#### Using a Slider to allow the user to change the year and a button for animation

Here we see how we can seamlessly integrate `bqplot` into the jupyter widget infrastructure. 

```python
year_slider = IntSlider(min=1800, max=2008, step=1, description='Year', value=initial_year)
```

When the `hovered_point` of the `Scatter` plot is changed (i.e. when the user hovers over a different element), the entire path of that country is displayed by making the `Lines` object visible and setting it's `x` and `y` attributes.

```python
def hover_changed(change):
    if change.new is not None:
        nation_line.x = data[data['name'] == wealth_scat.names[change.new]]['income'].values[0]
        nation_line.y = data[data['name'] == wealth_scat.names[change.new]]['lifeExpectancy'].values[0]
        nation_line.visible = True
    else:
        nation_line.visible = False
        
wealth_scat.observe(hover_changed, 'hovered_point')
```

On the slider value `callback` (a function that is triggered everytime the `value` of the slider is changed) we change the `x`, `y` and `size` co-ordinates of the `Scatter`. We also update the `text` of the `Label` to reflect the current year.

```python
def year_changed(change):
    wealth_scat.x, wealth_scat.y, wealth_scat.size = get_data(year_slider.value)
    year_label.text = [str(year_slider.value)]

year_slider.observe(year_changed, 'value')
```

#### Add an animation button

```python
play_button = Play(min=1800, max=2008, interval=time_interval)
jslink((play_button, 'value'), (year_slider, 'value'))
```

#### Displaying the GUI

```python
VBox([HBox([play_button, year_slider]), fig])
```
