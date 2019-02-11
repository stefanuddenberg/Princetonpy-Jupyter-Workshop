# General Code Formatting

- Use [Black](https://github.com/ambv/black) with Python 3.6+. `pip install black`
  - Install to Jupyter notebook with `jupyterlab_code_formatter`
    - Installation:
      ```
      jupyter labextension install @ryantam626/jupyterlab_code_formatter
      pip install jupyterlab_code_formatter
      jupyter serverextension enable --py jupyterlab_code_formatter
      ```
  - Can use the following keyboard shortcut (in User Overrides under Settings --> Advanced Settings Editor) to make it so that Black is applied to the cell when you press 'F' on cell focus
    ```json
    {
      "jupyterlab_code_formatter:black": {
        "command": "jupyterlab_code_formatter:black",
        "keys": ["F"],
        "selector": ".jp-Notebook:focus"
      }
    }
    ```

# Using Jupyter with git

- [Very helpful article](https://towardsdatascience.com/version-control-with-jupyter-notebooks-f096f4d7035a).
- Use `jupytext` to save notebook as equivalent Rmarkdown notebook. [Repo here](https://github.com/mwouts/jupytext).

  - Will need to create Jupyter config file if none exists: `jupyter notebook --generate-config`
  - Then add the following to `.jupyter/jupyter_notebook_config.py`:
    ```
    c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
    c.ContentsManager.default_jupytext_formats = "ipynb,md"
    ```
  - Can also add the following to make it output in [percent](https://github.com/mwouts/jupytext#the-percent-format) format: `c.ContentsManager.preferred_jupytext_formats_save = "py:percent"`
  - Can also [configure on a per-notebook basis](https://github.com/mwouts/jupytext#-per-notebook-configuration).

- Use Jupyter extension (fork by Yu Zhang) for VS Code (not as good as using actual Jupyter, though).

# Using Jupyter as an Educator

- Use [nbgrader](https://github.com/jupyter/nbgrader) to create, assign, collect, and (automatically) grade assignments.
