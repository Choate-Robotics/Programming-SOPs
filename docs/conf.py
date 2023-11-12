
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Programming Standard Operating Procedure'
copyright = '2023, Sebastian Plunkett'
author = 'Sebastian Plunkett'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_design', 'sphinx.ext.graphviz','sphinxcontrib.plantuml']

# path = 'java -jar ../utils/plantuml.jar'

# plantuml = path

# # PlantUML output format (default is 'png')
# plantuml_output_format = 'png'




templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']
html_logo = "7407logo.jfif"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'show_breadcrumbs': True,
}
html_favicon = "7407logo.jfif"