from crate.theme.rtd.conf.crate_guide import *

exclude_patterns = ["out/**"]

# crate.theme sets html_favicon to favicon.png which causes a warning because
# it should be a .ico and in addition there is no favicon.png in this project
# so it can't find the file
html_favicon = None

site_url = 'https://crate.io/docs/crate/guide/en/latest/'
extensions = ['sphinx_sitemap']
