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
    'logo_only': False,       # 显示 logo + 项目名称
    'display_version': False, # 不显示版本号
}

# ===== 蓝白简约风样式 =====
def setup(app):
    app.add_css_file(None, body="""
    /* ==== 蓝白简约风导航栏 ==== */
    .wy-nav-side {
        background: #ffffff !important;   /* 白色背景 */
        border-right: 1px solid #e6e6e6; /* 灰色分隔线 */
    }

    .wy-side-nav-search {
        background: #0066cc !important;  /* 蓝色顶部条 */
        padding: 15px !important;
    }

    .wy-side-nav-search > a {
        color: #ffffff !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    .wy-side-nav-search input[type="text"] {
        border-radius: 6px;
        border: none;
        padding: 6px;
    }

    .wy-menu-vertical a {
        color: #333333 !important;       /* 深灰文字 */
        font-size: 15px !important;
    }

    .wy-menu-vertical a:hover {
        background-color: #f0f8ff !important;  /* 淡蓝背景 */
        color: #0066cc !important;
    }

    .wy-menu-vertical li.current > a {
        background-color: #0066cc !important;
        color: #ffffff !important;
        font-weight: bold !important;
    }
    """)
