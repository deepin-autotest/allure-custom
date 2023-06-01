import os
import re


class _Setting:
    """配置模块"""

    _root_dir = os.path.dirname(os.path.abspath(__file__))
    _default_allure_path = os.path.join(_root_dir, "default_allure")
    _custom_allure_path = os.path.join(_root_dir, "allure")
    _allure_cli_path = os.path.join(_custom_allure_path, "bin/allure")
    _allure_config_path = os.path.join(_custom_allure_path, "config")
    _custom_allure_plugins_path = os.path.join(_custom_allure_path, "plugins")
    _custom_plugin_static_path = os.path.join(
        _custom_allure_plugins_path, "custom-logo-plugin/static"
    )

    static = os.path.join(_root_dir, "static")
    logo_png = os.path.join(_root_dir, "static", "logo.png")
    favicon_ico = os.path.join(_root_dir, "static", "favicon.ico")

    logo_height = "50px"
    sidebar_color = "#21483F"
    sidebar_line_size = "3px"
    sidebar_line_color = "#DEA400"

    html_title = "Funny_Test"
    report_name = "Funny_Test"
    report_language = "zh"


setting = _Setting()
