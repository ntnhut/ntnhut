# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Nhut Nguyen'
copyright = '2023, Nhut Nguyen'
author = 'Nhut Nguyen'

# release = '0.1'
# version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'furo'
html_title = 'Nhut Nguyen'
# html_logo = "nhut_transparent.png"
html_theme_options = {
    # 'logo_only': True,
    # "sidebar_hide_name": True,
    # 'nosidebar': True,
    "announcement": "Support my work by buying my books <a href='https://store.nhutnguyen.com'  target='_blank'>here</a>!", 
}


# -- Options for EPUB output
# epub_show_urls = 'footnote'
