from allure_custom import AllureCustom

from allure_custom.conf import setting

# 配置你的static静态文件
# setting.static = "~/static"
# setting.logo_png = "logo.png"

# 同步你的配置
AllureCustom.allure_custom()
#
# # 生成html测试报告
AllureCustom.gen("~/Desktop", "~/Desktop/html")
#
# # 打开html测试报告
AllureCustom.open("~/Desktop/html")
