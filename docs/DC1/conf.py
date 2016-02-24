import sys
import os

execfile (os.path.abspath("../conf.py"))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# If true, links to the reST sources are added to the pages.
html_copy_source = False
html_show_sourcelink = False