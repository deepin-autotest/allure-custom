import os
from allure_custom.setting import setting


class AllureCustom:

    @staticmethod
    def add_custom_plugin():
        os.system(f"cp {setting.static}/allure.yml {setting._allure_config_path}/")

    @staticmethod
    def update_css():
        os.system(f"cp {setting.static}/styles.css {setting._custom_plugin_static_path}/")

    @staticmethod
    def add_logo():
        os.system(f"cp {setting.static}/{setting.logo_png} {setting._custom_plugin_static_path}/")

    @classmethod
    def allure_custom(cls):
        os.system(f"rm -rf {setting._custom_allure_path}")
        os.system(f"cp -r {setting._default_allure_path} {setting._custom_allure_path}")
        cls.add_custom_plugin()
        cls.update_css()
        cls.add_logo()
        print("配置已刷新！")


    @classmethod
    def serve(cls, report_path):
        os.system(f"bash {setting._allure_cli_path} serve {report_path}")

    @classmethod
    def gen(cls, report_path: str, gen_html_path: str):
        if not gen_html_path:
            gen_html_path = setting.static
        os.system(f"bash {setting._allure_cli_path} generate {report_path}/ -o {gen_html_path}/")

    @classmethod
    def open(cls, gen_report_path):
        os.system(f"bash {setting._allure_cli_path} open {gen_report_path}/")
