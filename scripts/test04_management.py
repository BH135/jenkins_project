import os
import allure
import pytest
from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_management import Management
from tool.get_logger import GetLogger

log = GetLogger().get_logger()

class TestManagement():

    # 定义 setup
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化 PageKnowledgeBase页面
        self.management = Management(self.driver)
        # 调用成功登录 依赖
        PageLogin(self.driver).page_login()

    def teardown_class(self):
        GetDriver().quit_driver()

    @allure.feature("绿色数字城市CIM基础平台")
    @allure.story("资料管理")
    @allure.title("文件管理模块功能点测试")
    @allure.description("此条用例针对资料管理模块下文件管理模块的增删改查测试")
    def test_add_management(self):
        # 调用 组合业务方法-01  此方法为了断言业务是否新增成功
        self.management.page_management_one()
        # 断言是否新增成功
        msg = self.management.page_get_text_new()
        assert msg, "测试"

        # 调用 组合业务方法-02  此方法为了断言业务是否上传成功
        self.management.page_management_tow()
        # 断言是否新增成功
        msg = self.management.page_get_file()
        assert msg, "城市项目.xlsx"

        # # 调用 组合业务方法-03  此方法为了断言业务是否移动成功
        # self.management.page_management_three()
        # # 断言是否新增成功
        # msg = self.management.page_move_results()
        # self.assertEqual(msg, "城市项目.xlsx")

if __name__=="__main__":
    pytest.main(['-s', '-q', '--alluredir', 'report'])
    os.system("allure generate report/ -o html --clean")