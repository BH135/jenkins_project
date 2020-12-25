import os

import allure
import pytest
from parameterized import parameterized
from base.get_driver import GetDriver
from page.page_knowledgebase import KnowledgeBase
from page.page_login import PageLogin
from tool.read_txt_kb import read_txt
from tool.get_logger import GetLogger

log = GetLogger().get_logger()

def get_data():
    arrs = []
    for data in read_txt():
        arrs.append(tuple(data.strip().split(",")))

    return arrs[1::]

# 定义测试类
class TestKnowledgeBase():
    # 定义 setup
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化 PageKnowledgeBase页面
        self.kb = KnowledgeBase(self.driver)
        # 调用成功登录 依赖
        PageLogin(self.driver).page_login()

    def teardown_class(self):

        GetDriver().quit_driver()

    @parameterized.expand(get_data())
    @allure.feature("绿色数字城市CIM基础平台")
    @allure.story("知识库")
    @allure.title("政策管理模块功能点测试")
    @allure.description("此条用例针对知识库模块下政策管理模块的增删改查测试")
    def test_add_KnowledgeBase(self, title, source, content):
        # 调用 组合业务方法-01  此方法为了断言上传文件是否成功
        self.kb.page_knowledgebase_one(title, source)
        # 断言是否上传成功
        msg = self.kb.page_get_text_upload()
        assert msg, "城市项目.xlsx"

        # 调用 组合业务方法-02  此方法为了断言业务是否新增成功
        self.kb.page_knowledgebase_two(content)
        # 断言是否新增成功
        msg = self.kb.page_get_text_new()
        assert msg, "ProjectTesting"

        #调用 组合业务方法-03 次方法断言搜索结果
        self.kb.page_knowledgebase_three(title)
        # 断言搜索结果
        msg = self.kb.page_get_text_search()
        assert msg, "ProjectTesting"

        # 调用 组合业务方法-04 次方法断言搜索来结果
        self.kb.page_knowledgebase_four(source)
        # 断言搜索结果
        msg = self.kb.page_get_text_search()
        assert msg, "ProjectTesting"

        # 调用 组合业务方法-05 此方法用于测试成功后进行测试业务删除操作
        self.kb.page_delete()

if __name__=="__main__":
    pytest.main(['-s', '-q', '--alluredir', 'report'])
    os.system("allure generate report/ -o html --clean")