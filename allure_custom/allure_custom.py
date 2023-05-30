import os
from allure_custom.setting import setting


class AllureCustom:

    @staticmethod
    def add_custom_plugin():
        os.system(f"cp {setting.static}/allure.yml {setting.allure_config_path}/")

    @staticmethod
    def update_css():
        os.system(f"cp {setting.static}/styles.css {setting.custom_plugin_static_path}/")

    @staticmethod
    def add_logo():
        os.system(f"cp {setting.static}/logo.png {setting.custom_plugin_static_path}/")

    @classmethod
    def allure_custom(cls):
        os.system(f"rm -rf {setting.custom_allure_path}")
        os.system(f"cp -r {setting.default_allure_path} {setting.custom_allure_path}")
        cls.add_custom_plugin()
        cls.update_css()
        cls.add_logo()



if __name__ == '__main__':
    AllureCustom.allure_custom()

