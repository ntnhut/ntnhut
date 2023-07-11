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
# html_logo = "nhut_transparent.png"
html_theme_options = {
    # 'logo_only': True,
    # "sidebar_hide_name": True,
    # 'nosidebar': True,
    "announcement": "Check out <a href='https://store.nhutnguyen.com/l/nhutnguyen_resume'  target='_blank'>my resume</a> for FREE!", 
}


# -- Options for EPUB output
# epub_show_urls = 'footnote'
