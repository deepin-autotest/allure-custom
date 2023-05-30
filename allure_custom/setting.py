import os


class _Setting:
    """配置模块"""

    root_dir = os.path.dirname(os.path.abspath(__file__))
    static = os.path.join(root_dir, "static")
    default_allure_path = os.path.join(root_dir, "default_allure")

    custom_allure_path = os.path.join(root_dir, "allure")
    allure_cli_path = os.path.join(custom_allure_path, "bin/allure")
    allure_config_path = os.path.join(custom_allure_path, "config")
    custom_allure_plugins_path = os.path.join(custom_allure_path, "plugins")
    custom_plugin_static_path = os.path.join(custom_allure_plugins_path, "custom-logo-plugin/static")


setting = _Setting()
