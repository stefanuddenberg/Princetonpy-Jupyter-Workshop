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

# Using R and MATLAB in Jupyter with Python


# Run R code
Note that this requires running from a Python 3 instance of Jupyter (in my case, at least).


## R for Jupyter installation instructions:
In theory, you should just be able to run this line and be all set, but it didn't work for me: `conda install -c r r-essentials`
<br><br>
If that didn't work, go through these steps:
- In R (not RStudio), run the following:
# ```R
install.packages('devtools')
devtools::install_github('IRkernel/IRkernel')
IRkernel::installspec()  # to register the kernel in the current R installation
# ```
- make sure you have R added to your PATH (in my case, C:\Program Files\R\R-3.3.3\bin\x64)
    - _Windows_: Need R_HOME (same path as above) and R_USER (just your windows user name) added as separate environment vars
- Install libraries like ggplot2 directly into R itself, not RStudio: `install.packages('ggplot2', dependencies=TRUE)`
- _Mac/Linux_: Run `pip install rpy2` from your command line/terminal
    - _Windows_: [get appropriate installation from here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2), and run `pip install rpy2‑2.8.6‑cp36‑cp36m‑win_amd64.whl` or whatever your .whl file is called from within the directory that has the file.
        - You may also need to add the following two directories to your PATH: C:\Anaconda3\Library\mingw-w64\bin; C:\Anaconda3\Library\mingw-w64\lib
- [See here for further information if needed](https://github.com/IRkernel/IRkernel)


# Example Python to R pipeline
First, make some example data in Python.

```python
import pandas as pd

df = pd.DataFrame(
    {
        "Letter": ["a", "a", "a", "b", "b", "b", "c", "c", "c"],
        "X": [4, 3, 5, 2, 1, 7, 7, 5, 9],
        "Y": [0, 4, 3, 6, 7, 10, 11, 9, 13],
        "Z": [1, 2, 3, 1, 2, 3, 1, 2, 3],
    }
)
```

Load extension allowing one to run R code from within a Python notebook.

```python
%load_ext rpy2.ipython
```

Do stuff in R with cell or line magics. "-i" imports to R, "-o" outputs from R back to Python.

```python
# %%R
# install.packages("ggplot2", dep=TRUE)
# install.packages("tidyr", dep=TRUE)
# install.packages("dplyr", dep=TRUE)
# install.packages("tidyverse", dep=TRUE)
```

```R
library("ggplot2")
ggplot(data = df) + geom_point(aes(x = X, y = Y, color = Letter, size = Z))
```

```R
install.packages("rlang")
```

# Run Javascript code

```javascript
console.log('hey!')
```
