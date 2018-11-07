import os
import yaml

from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser

master_doc = 'index'
html_theme = 'redirect_template'
html_theme_path = ['.']

source_parsers = {
    '.md': CommonMarkParser,
}

# -- AutoStructify --------------------------------------------------------
def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True,
        'enable_auto_doc_ref': True
    }, True)
    app.add_transform(AutoStructify)

try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'redirect.yml')) as redirect:
        redirect_data = redirect.read()
        redirect_data = yaml.safe_load(redirect_data)
except:
    pass


html_context = redirect_data
