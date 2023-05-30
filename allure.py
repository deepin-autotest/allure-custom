import os
import sys

root_dir = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(root_dir, "static")

allure_cli_path = os.path.join(root_dir, "allure/bin/allure")
allure_config_path = os.path.join(root_dir, "allure/config")
allure_plugins_path = os.path.join(root_dir, "allure/plugins")
custom_plugin_static_path = os.path.join(allure_plugins_path, "custom-logo-plugin/static")

back_path = os.path.join(root_dir, "back_allure")

os.system(f"cp -r {root_dir}/allure {back_path}")


def add_custom_plugin():
    os.system(f"cp {static_path}/allure.yml {allure_config_path}/")


def update_css():
    os.system(f"cp {static_path}/styles.css {custom_plugin_static_path}/")


def add_logo():
    os.system(f"cp {static_path}/logo.png {custom_plugin_static_path}/")
