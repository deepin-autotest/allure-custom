# allure-custom

定制 Allure 报告

目前支持的定制项：

1. logo

2. 标题栏文案

3. 侧边栏颜色

4. 默认暂时的语言

---

**Documentation**: <a href="https://funny-dream.github.io/allure-custom" target="_blank">https://funny-dream.github.io/allure-custom</a>

**Source Code**: <a href="https://github.com/funny-dream/allure-custom" target="_blank">https://github.com/funny-dream/allure-custom</a>

---

## 安装

```shell
pip install allure-custom
```

## 配置

```python hl_lines="1 4 6 22 26 30"
from allure_custom.conf import setting

# 测试报告的title
setting.html_title = "funny_test"
# 测试报告的name
setting.report_name = "Funny_Test"

# 测试报告的默认语言
# en:English
# ru:Русский
# zh:中文
# de:Deutsch
# nl:Nederlands
# he:Hebrew
# br:Brazil
# pl:Polski
# ja:日本語
# es:Español
# kr:한국어
# fr:Français
# az:Azərbaycanca
setting.report_language = "zh"

# 左上角 logo 图片
# 注意这里给一个绝对路径
setting.logo_png = "/home/xxx/logo.png"

# html favicon
# 注意这里给一个绝对路径
setting.favicon_ico = "/home/xxx/favicon.ico"
```

## 使用方法

```python hl_lines="1 5 8 11"
from allure_custom import AllureCustom

# 生成html测试报告
# ~/Desktop/report 此目录下保存了allure的json\txt的报告文件
AllureCustom.gen(report_path="~/Desktop/report", generate_allure_html="~/Desktop/html")

# 打开html测试报告
AllureCustom.open(generate_allure_html="~/Desktop/html")

# 直接生成在线测试报告
AllureCustom.serve(report_path="~/Desktop/report")
# 根据终端输出提示的在线链接，在浏览器查看即可；
```

## 效果展示

<p align="center">
  <a href="https://github.com/funny-dream/allure-custom"><img src="https://raw.githubusercontent.com/funny-dream/allure-custom/main/docs/img/index.png" alt="allure-custom"></a>
</p>
