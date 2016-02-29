# -*- coding: utf-8 -*-
#
# Realeyes Developer Portal documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 24 14:42:44 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import sphinx_rtd_theme

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.pngmath',
    'sphinx.ext.ifconfig',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Realeyes Developer Portal'
copyright = u'Copyright 2016 © Realeyes Data Services Ltd.'
author = u'Realeyes'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0'

language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

html_theme = 'alabaster'

html_title = u''
# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_favicon = 'favicon.ico'

# Output file base name for HTML help builder.
htmlhelp_basename = 'RealeyesDeveloperPortaldoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'RealeyesDeveloperPortal.tex', u'Realeyes Developer Portal Documentation',
     u'Realeyes', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'realeyesdeveloperportal', u'Realeyes Developer Portal Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'RealeyesDeveloperPortal', u'Realeyes Developer Portal Documentation',
     author, 'RealeyesDeveloperPortal', 'One line description of project.',
     'Miscellaneous'),
]


# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'https://docs.python.org/': None}
