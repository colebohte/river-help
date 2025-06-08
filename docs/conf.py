# docs/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'river-help'
author = 'River Games'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',  # if you're using Markdown
]

templates_path = ['_templates']
exclude_patterns = []

# ✨ Set the Furo theme
html_theme = 'furo'

# (Optional) Custom logo and favicon
# html_logo = '_static/logo.png'
# html_favicon = '_static/favicon.ico'

html_static_path = ['_static']
