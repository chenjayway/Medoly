# -*- coding: utf-8 -*-
import pkg_resources

version = release = "0.1.0a"

extensions = ['sphinx.ext.autodoc']

source_suffix = '.rst'  # The suffix of source filenames.
master_doc = 'index'  # The master toctree document.

project = 'Modaly Doc'
copyright = '2016, Euterpe and contributors'
exclude_patterns = ['jsonrpc-example-code/*']


# index - master document
# rst2pdf - name of the generated pdf
# Sample rst2pdf doc - title of the pdf
# Your Name - author name in the pdf

pdf_documents = [('index', u'rst2pdf', project, u'Lianghui Huang'), ]


import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# html_theme = "bizstyle"
# html_theme_options = {
#     "rightsidebar": "true",
#     "relbarbgcolor": "black"
# }


modindex_common_prefix = ['demo.']

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True


# html_favicon = ...
html_add_permalinks = False
# html_show_sourcelink = True # ?set to False?

# Content template for the index page.
#html_index = ''

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Output file base name for HTML
