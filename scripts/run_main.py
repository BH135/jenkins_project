# 导包
import unittest
import time
from HwTestReport.HwTestReport import HTMLTestReport


# 用例执行目录
suite = unittest.defaultTestLoader.discover("../scripts")
# 报告生成目录及文件名称
dir_path = "../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# 获取文件流并调用run运行
with open(dir_path, "wb") as f:
    runner = HTMLTestReport(stream=f,
                            verbosity=2,
                            title='绿色数字城市CIM基础平台自动化测试',
                            description='运行环境：win10',
                            tester='B.H')

    runner.run(suite)