# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import numpydoc.docscrape as np_docscrape


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'my_package'
copyright = '2023, Tirth Patel'
author = 'Tirth Patel'
release = '0.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']


# -- Extensions --------------------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'numpydoc'
]


# -- Autosummary Configurations ----------------------------------------------

autosummary_generate = True


# -- Numpy extension Configurations ------------------------------------------

# If we want to do a phantom import from an XML file for all autodocs
# phantom_import_file = 'dump.xml'

# Generate plots for example sections
numpydoc_use_plots = True
np_docscrape.ClassDoc.extra_public_methods = [  # should match class.rst
    '__call__', '__mul__', '__getitem__', '__len__',
]


# -- Autodoc Configurations --------------------------------------------------

autodoc_default_options = {
    'inherited-members': None,
}
