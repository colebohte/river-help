# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # so Sphinx can find your Python code

project = 'river-help'
copyright = '2025, River Games'
author = 'River Games'

release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',  # only if you're using .md files
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
