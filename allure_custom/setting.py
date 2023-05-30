import os

def check_path(file):
    if not os.path.exists(file):
        raise FileNotFoundError(f"{file}不存在！")


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
    logo_png = "logo.png"
    check_path(static)
    check_path(f"{static}/{logo_png}")


setting = _Setting()
