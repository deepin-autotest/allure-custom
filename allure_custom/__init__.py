import json
import os
import re
from time import sleep
from datetime import datetime

from allure_custom.conf import setting


class AllureCustom:
    """定制报告"""

    @staticmethod
    def add_custom_plugin():
        if not os.path.exists(setting.static):
            raise FileNotFoundError
        os.system(f"cp {setting.static}/allure.yml {setting._allure_config_path}/")

    @staticmethod
    def update_css():
        os.system(
            f"cp {setting.static}/styles.css {setting._custom_plugin_static_path}/"
        )

        with open(
                f"{setting._custom_plugin_static_path}/styles.css", "r", encoding="utf-8"
        ) as f:
            style_css = f.read()
        style_css = re.sub(r"{{logo_height}}", setting.logo_height, style_css)
        style_css = re.sub(r"{{sidebar_color}}", setting.sidebar_color, style_css)
        style_css = re.sub(
            r"{{sidebar_line_size}}", setting.sidebar_line_size, style_css
        )
        style_css = re.sub(
            r"{{sidebar_line_color}}", setting.sidebar_line_color, style_css
        )

        with open(
                f"{setting._custom_plugin_static_path}/styles.css", "w", encoding="utf-8"
        ) as f:
            f.write(style_css)

    @staticmethod
    def add_logo():
        if not os.path.exists(setting.logo_png):
            raise FileNotFoundError
        os.system(f"cp {setting.logo_png} {setting._custom_plugin_static_path}/")

    @staticmethod
    def check_copy(*dirs):
        res = {}
        for i in dirs:
            if not os.path.exists(i):
                raise FileNotFoundError(i)
            default_files = []
            for root, dirs, files in os.walk("default_allure"):
                for file in files:
                    if file.endswith(".jar"):
                        default_files.append(file)
            res[i] = default_files

        res = [len(i) for i in res.values()]
        if len(set(res)) == 1:
            return True
        return False


    @classmethod
    def allure_custom(cls):
        os.system(f"rm -rf {setting._custom_allure_path}")
        os.system(f"mkdir -p {setting._custom_allure_path}")
        os.system(f"cp -r {setting._default_allure_path}/* {setting._custom_allure_path}/")

        for i in range(10):
            if cls.check_copy(setting._default_allure_path, setting._custom_allure_path):
                break
            sleep(1)

        cls.add_custom_plugin()
        cls.update_css()
        cls.add_logo()
        # print("配置已刷新！")


    @classmethod
    def gen(cls, report_path: str, generate_allure_html: str, clean: bool = False):
        if not generate_allure_html:
            generate_allure_html = setting.static
        cls.allure_custom()
        os.system(
            f"bash {setting._allure_cli_path} generate {report_path}/ -o {generate_allure_html}/ {'--clean' if clean else ''}"
        )
        sleep(3)
        # title
        with open(
                os.path.expanduser(f"{generate_allure_html}/index.html"),
                "r",
                encoding="utf-8",
        ) as _f:
            html = _f.read()
        re_html = re.sub(
            r"<title>Allure Report</title>",
            f"<title>{setting.html_title}</title>",
            html,
        )
        with open(
                os.path.expanduser(f"{generate_allure_html}/index.html"),
                "w",
                encoding="utf-8",
        ) as _f:
            _f.write(re_html)
        sleep(1)
        # 语言
        with open(
                os.path.expanduser(f"{generate_allure_html}/app.js"), "r", encoding="utf-8"
        ) as _f:
            _js = _f.read()
        re_js = re.sub(r'language:"en"', f'language:"{setting.report_language}"', _js)
        with open(
                os.path.expanduser(f"{generate_allure_html}/app.js"), "w", encoding="utf-8"
        ) as _f:
            _f.write(re_js)
        sleep(1)
        # 内容title
        with open(
                os.path.expanduser(f"{generate_allure_html}/widgets/summary.json"),
                "r",
                encoding="utf-8",
        ) as _f:
            summary = json.load(_f)
            summary["reportName"] = setting.report_name
        with open(
                os.path.expanduser(f"{generate_allure_html}/widgets/summary.json"),
                "w",
                encoding="utf-8",
        ) as _f:
            json.dump(summary, _f, ensure_ascii=False, indent=4)
        sleep(1)
        # html ico
        os.system(f"cp -f {setting.static}/favicon.ico {generate_allure_html}/")

    @classmethod
    def open(cls, generate_allure_html):
        os.system(f"bash {setting._allure_cli_path} open {generate_allure_html}/")

    @classmethod
    def serve(cls, report_path):
        generate_allure_html_tmp = f"/tmp/allure_{datetime.now().strftime('%m%d%p%I%M%S')}"
        cls.gen(report_path=report_path, generate_allure_html=generate_allure_html_tmp)
        cls.open(generate_allure_html_tmp)
