import os
import pytest
import allure
from base.get_driver import GetDriver
from page.page_login import PageLogin
from tool.get_logger import GetLogger
from tool.read_txt_filestore import read_txt

log = GetLogger().get_logger()



# 新建 登录测试类 并 继承 unittest.TestCase
class TestLogin():

    # setUp
    def setup_class(self):
        try:
            # 实例化 获取页面对象 PageLogin
            self.login = PageLogin(GetDriver().get_driver())
        except Exception as e:
            log.error("错误：{}".format(e))

    # tearDown
    def teardown_class(self):
        # 关闭 driver驱动对象pytest.ini
        GetDriver().quit_driver()

    # 登录测试方法
    @pytest.mark.parametrize(("username", "pwd", "expect_result"),[("admin", "tydt_12345", "系统管理员")])
    @allure.feature("绿色数字城市CIM基础平台")
    @allure.story("用户登录")
    @allure.title("输入正确用户名和密码登录测试")
    @allure.description("此条用例针对绿色数字城市CIM基础平台下登录模块测试")
    def test_login(self,username, pwd, expect_result):
        # 调用登录方法
        self.login.page_login(username, pwd)
        # 获取登录提示信息
        msg = self.login.page_get_error_info()
        # 断言
        try:
            assert msg==expect_result
        except Exception as e:
            # 截图
            with allure.step('异常截图'):
                self.login.base_get_image1()
                log.error("错误：{}".format(e))

if __name__=="__main__":
    pytest.main(['-s', '-q', '--alluredir', 'report'])
    os.system("allure generate report/ -o html --clean")

