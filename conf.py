# -- Project information -----------------------------------------------------

project = 'test'
copyright = '2018, tom'
author = 'tom'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''

extensions = [
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
]

source_suffix = '.rst'
master_doc = 'index'
html_static_path = ['_static']

ipython_warning_is_error = False


def setup(app):
    app.add_js_file("js/whatsnew_redirect.js")
