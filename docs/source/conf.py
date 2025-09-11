# -- Project information -----------------------------------------------------
project = 'Smart Home Quick Start Guide'
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

# 主题选项
html_theme_options = {
    'logo_only': False,        # 显示 logo + 项目名称
    'display_version': False,  # 不显示版本号
    'navigation_depth': 4,     # 导航层级
    'collapse_navigation': False,
    'style_nav_header_background': "#2980B9",  # 顶部蓝色
}

# 内嵌 CSS 样式（蓝白简约 + 导航高亮 + 选中项左侧竖线）
def setup(app):
    app.add_css_file(None, body="""
        body {
            background-color: #ffffff;
            color: #333333;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        a {
            color: #2980B9;
        }
        .wy-side-nav-search {
            background-color: #f5f5f5;
        }
        .wy-nav-side {
            background-color: #ffffff;
        }
        /* 鼠标悬停时高亮 */
        .wy-menu-vertical a:hover {
            background-color: #e6f2fa;
            color: #007ACC;
        }
        /* 当前选中项高亮 + 左边竖线 */
        .wy-menu-vertical .current > a,
        .wy-menu-vertical .current > a:hover {
            background-color: #f0f8ff;
            color: #2980B9;
            font-weight: bold;
            border-left: 4px solid #2980B9;
            padding-left: 12px; /* 让文字不会紧贴竖线 */
        }
    """)
