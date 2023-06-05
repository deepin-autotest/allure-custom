from allure_custom import AllureCustom
from allure_custom.conf import setting

# 配置你的static静态文件
# setting.static = "~/static"
# setting.logo_png = "logo.png"

# 生成html测试报告
AllureCustom.gen(report_path="~/Desktop/report", generate_allure_html="~/Desktop/html")

# 打开html测试报告
AllureCustom.open(generate_allure_html="~/Desktop/html")

# 直接生成在线测试报告
AllureCustom.serve(report_path="~/Desktop/report")
