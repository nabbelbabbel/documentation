#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

def setup(app):
    app.add_stylesheet("main_stylesheet.css")

extensions = [
    'breathe', 
    'sphinx.ext.mathjax', 
    'm2r'
]
breathe_projects = { 
    "core"    : "../build/xml/core",
    "sparrow" : "../build/xml/sparrow",
    "readuct" : "../build/xml/readuct",
    "utilities": "../build/xml/utilities" 
}
templates_path = ['_templates']
html_static_path = ['_static']
source_suffix = [ '.rst', '.md']
master_doc = 'index'
project = 'SCINE'
copyright = '2019, Reiher Group'
author = 'Reiher Group'
html_logo = 'scine_logo_white.svg'
exclude_patterns = []
highlight_language = 'c++'
pygments_style = 'sphinx'
todo_include_todos = False
htmlhelp_basename = 'scinedoc'
