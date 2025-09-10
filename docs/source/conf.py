# -- Project information -----------------------------------------------------
project = 'LA_Smart_Home-Installation tutorial'
copyright = '2025, Lafvin'
author = 'Lafvin'

# -- General configuration ---------------------------------------------------
extensions = ["myst_parser"]

from pygments.lexers import Python3Lexer
pygments_lexers = {
    "python-repl": Python3Lexer(),
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# 指定 logo 图片（放在 docs/_static/Logo2.png）
html_logo = "_static/Logo2.png"

# 启用静态文件目录（logo / css）
html_static_path = ['_static']

# 主题选项（注意 logo_only = False）
html_theme_options = {
    'logo_only': False,       # 显示 logo + 项目名称
    'display_version': False, # 不显示版本号
}

# 自定义 CSS（调整 logo 和文字对齐）
html_css_files = [
    'css/custom.css',
]
