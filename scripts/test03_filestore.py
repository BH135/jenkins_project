import os

import pytest
import allure
from parameterized import parameterized
from base.get_driver import GetDriver
from page.page_filestore import FileStore
from page.page_login import PageLogin
from tool.read_txt_filestore import read_txt
from tool.get_logger import GetLogger

log = GetLogger().get_logger()

def get_data():
    arrs = []
    for data in read_txt():
        arrs.append(tuple(data.strip().split(",")))

    return arrs[1::]

class TestFileStore():
    # 定义 setup
    def setup_class(self):
        self.imgs = []
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化 PageKnowledgeBase页面
        self.filestore = FileStore(self.driver)
        # 调用成功登录 依赖
        PageLogin(self.driver).page_login()

    def teardown_class(self):

        GetDriver().quit_driver()

    @parameterized.expand(get_data())
    @allure.feature("绿色数字城市CIM基础平台")
    @allure.story("文件存储")
    @allure.title("空间管理模块功能点测试")
    @allure.description("此条用例针文件存储模块下空间管理模块的增删改查测试")
    def test_add_KnowledgeBase(self, Spacename, Searchname):
        # 调用 组合业务方法-01  此方法为了断言业务是否新增成功
        self.filestore.page_filestore_one(Spacename)
        # 断言是否新增成功
        msg = self.filestore.page_get_text_new()
        assert msg, "LSSZ"

        # 调用 组合业务方法-02  此方法为了断言文件是否上传成功
        self.filestore.page_filestore_three()
        # 断言是否上传成功
        msg = self.filestore.page_get_file()
        assert msg, "城市项目.xlsx"

        # 调用 组合业务方法-03  此方法用于删除测试数据
        self.filestore.page_filestore_four()

if __name__=="__main__":
    pytest.main(['-s', '-q', '--alluredir', 'report'])
    os.system("allure generate report/ -o html --clean")