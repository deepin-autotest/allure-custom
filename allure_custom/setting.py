import os


class _Setting:
    """配置模块"""

    _root_dir = os.path.dirname(os.path.abspath(__file__))
    _default_allure_path = os.path.join(_root_dir, "default_allure")
    _custom_allure_path = os.path.join(_root_dir, "allure")
    _allure_cli_path = os.path.join(_custom_allure_path, "bin/allure")
    _allure_config_path = os.path.join(_custom_allure_path, "config")
    _custom_allure_plugins_path = os.path.join(_custom_allure_path, "plugins")
    _custom_plugin_static_path = os.path.join(_custom_allure_plugins_path, "custom-logo-plugin/static")

    static = os.path.join(_root_dir, "static")
    logo_png = os.path.join(_root_dir, "static", "logo.png")
    favicon_ico = os.path.join(_root_dir, "static", "favicon.ico")

    if not os.path.exists(static):
        static = os.path.join(_root_dir, "static")
    if not os.path.exists(f"{static}/{logo_png}"):
        logo_png = os.path.join(_root_dir, "static", "logo.png")
    if not os.path.exists(f"{static}/{favicon_ico}"):
        favicon_ico = os.path.join(_root_dir, "static", "favicon.ico")

    logo_height = "50px"
    sidebar_color = "#21483F"
    sidebar_line_size = "3px"
    sidebar_line_color = "#DEA400"
    with open(os.path.join(_root_dir, "static", "styles.css"), "r", encoding="utf-8") as f:
        style_css = f.read()
    style_css = style_css.format(
        logo_height=logo_height,
        sidebar_color=logo_height,
        sidebar_line_size=logo_height,
        sidebar_line_color=logo_height,
    )

    with open(os.path.join(_root_dir, "static", "styles.css"), "w", encoding="utf-8") as f:
        f.write(style_css)

    html_title = "funny_test"
    report_name = "funny_test"
    report_language = "zh"


setting = _Setting()
