import json
import os
import re
from time import sleep

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
        os.system(f"cp {setting.logo_png} {setting._custom_plugin_static_path}/")

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
    def gen(cls, report_path: str, generate_allure_html: str):
        if not generate_allure_html:
            gen_html_path = setting.static
        os.system(f"bash {setting._allure_cli_path} generate {report_path}/ -o {generate_allure_html}/")
        sleep(1)
        # title
        with open(f"{generate_allure_html}/index.html", "r", encoding="utf-8") as _f:
            html = _f.read()
        re_html = re.sub(
            r"<title>Allure Report</title>", f"<title>{setting.html_title}</title>", html
        )
        with open(
                f"{generate_allure_html}/index.html", "w", encoding="utf-8"
        ) as _f:
            _f.write(re_html)
        # 语言
        with open(f"{generate_allure_html}/app.js", "r", encoding="utf-8") as _f:
            _js = _f.read()
        re_js = re.sub(r'language:"en"', f'language:"{setting.report_language}"', _js)
        with open(
                f"{generate_allure_html}/app.js", "w", encoding="utf-8"
        ) as _f:
            _f.write(re_js)
        # 内容title
        with open(f"{generate_allure_html}/widgets/summary.json", "r", encoding="utf-8") as _f:
            summary = json.load(_f)
            summary["reportName"] = setting.report_name
        with open(
                f"{generate_allure_html}/widgets/summary.json",
                "w",
                encoding="utf-8",
        ) as _f:
            json.dump(summary, _f, ensure_ascii=False, indent=4)
        # html ico
        os.system(
            f"cp -f {setting.static}/favicon.ico {generate_allure_html}/"
        )

    @classmethod
    def open(cls, gen_report_path):
        os.system(f"bash {setting._allure_cli_path} open {gen_report_path}/")
