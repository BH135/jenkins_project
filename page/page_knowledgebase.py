from time import sleep
import allure
import page
from base.base import Base
from tool.get_logger import GetLogger

log = GetLogger().get_logger()

class KnowledgeBase(Base):

    sleep(2)
    @allure.step(title='点击CIM跳转至绿色数字城市CIM基础平台')
    def page_cim(self):
        sleep(2)
        self.base_click(page.currency_cim)

    # 知识库
    @allure.step(title='点击知识库')
    def page_click_kb(self):
        # 切换句柄
        self.base_switch_to_window(page.pay_my_prder_title)
        # 点击知识库
        self.base_click(page.kb)
        # 截图
        self.base_get_image()

    # 新增
    @allure.step(title='点击新增')
    def page_click_newlyadded(self):
        # 切换iframe表单
        self.base_switch_frame(page.currency_frame_name)
        # 点击新增
        sleep(2)
        self.base_click(page.kb_newlyadded_btn)
        # 截图
        self.base_get_image()

    # 标题
    @allure.step(title='输入标题')
    def page_send_keys_title(self, title):
        # 切换iframe1表单
        self.base_switch_frame(page.currency_frame_name1)
        # 输入标题
        sleep(2)
        log.info("[page_loging] 对：{} 元素 输入标题：{} 操作".format(page.kb_title,title))
        self.base_input(page.kb_title, title)
        # 截图
        self.base_get_image()

    # 输入来源
    @allure.step(title='输入来源')
    def page_send_keys_source(self, source):
        log.info("[page_loging] 对：{} 元素 输入来源：{} 操作".format(page.kb_source,source))
        self.base_input(page.kb_source, source)
        # 截图
        self.base_get_image()

    # 选择类型
    @allure.step(title='选择类型')
    def page_click_type(self):
        self.base_click(page.kb_type)
        self.base_get_image()

    # 发布时间
    @allure.step(title='选择发布时间')
    def page_click_releasetime(self):
        # 点击选择时间框
        self.base_click(page.kb_Releasetime)
        # 选择日期
        self.base_click(page.kb_Selectdate)
        # 截图
        self.base_get_image()

    # 文件
    @allure.step(title='上传文件')
    def page_click_selectfile(self):
        # 上传文件
        self.base_click(page.kb_Uploadfiles)
        # 切换iframe2表单
        self.base_switch_frame(page.currency_frame_name2)
        # 选择文件
        self.base_click(page.kb_Selectfile)
        sleep(3)
        # 开始上传文件操作
        self.base_uploadfiles()
        # 截图
        self.base_get_image()

    # 获取上传结果
    def page_get_text_upload(self):
        # 获取结果并返回
        log.info("[page_loging] 正在获取上传结果：{}".format(self.base_get_text(page.kb_Uploadfiles_result)))
        return self.base_get_text(page.kb_Uploadfiles_result)

    # 确定
    @allure.step(title='上传确定')
    def page_determine(self):
        # 退出iframe表单
        self.base_signout_switch_frame()
        # 切换iframe表单
        self.base_switch_frame(page.currency_frame_name)
        # 切换iframe1表单
        self.base_switch_frame(page.currency_frame_name1)
        # 点击确定
        self.base_click(page.kb_determine)
        # 截图
        self.base_get_image()

    # 输入内容
    @allure.step(title='输入内容')
    def page_content(self, content):
        log.info("[page_loging] 对：{} 元素 输入内容：{} 操作".format(page.kb_content, content))
        self.base_input(page.kb_content, content)
        # 截图
        self.base_get_image()

    # 确定
    @allure.step(title='新增业务确认测试')
    def page_determine1(self):
        # 退出iframe表单
        self.base_signout_switch_frame()
        # 切换iframe表单
        self.base_switch_frame(page.currency_frame_name)
        # 点击确定
        self.base_click(page.kb_determine1)
        # 截图
        self.base_get_image()

    # 获取业务新增结果
    def page_get_text_new(self):
        # 获取结果并返回
        return self.base_get_text(page.kb_newlyadded_result)

    # 标题搜索
    @allure.step(title='标题搜索测试')
    def page_search(self, title):
        self.base_input(page.kb_search, title)
        # 截图
        self.base_get_image()

    # 重置
    @allure.step(title='点击重置测试')
    def page_reset(self):
        self.base_click(page.kb_reset)
        # 截图
        self.base_get_image()

    # 来源搜索
    @allure.step(title='来源搜索测试')
    def page_source(self, source):
        self.base_input(page.kb_source, source)
        # 截图
        self.base_get_image()

    # 获取搜索结果
    def page_get_text_search(self):
        # 获取结果并返回
        return self.base_get_text(page.kb_search_result)

    # 测试完成删除业务
    @allure.step(title='删除测试业务')
    def page_delete(self):
        # 点击删除
        self.base_click(page.kb_delete)
        # 确认删除
        self.base_click(page.kb_todelete)
        # 截图
        self.base_get_image()

    # 组合业务方法-01
    def page_knowledgebase_one(self, title, source):
        self.page_cim()
        self.page_click_kb()
        self.page_click_newlyadded()
        self.page_send_keys_title(title)
        self.page_send_keys_source(source)
        self.page_click_type()
        self.page_click_releasetime()
        self.page_click_selectfile()
        self.page_get_text_upload()

    # 组合业务方法-02
    def page_knowledgebase_two(self,content):
        self.page_determine()
        self.page_content(content)
        self.page_determine1()
        sleep(3)
        self.page_get_text_new()

    # 组合业务方法-03
    def page_knowledgebase_three(self,title):
        self.page_search(title)
        self.page_get_text_search()

    # 组合业务方法-04
    def page_knowledgebase_four(self, source):
        sleep(2)
        self.page_reset()
        self.page_source(source)
        self.page_get_text_search()

    # 组合业务方法-05
    def page_knowledgebase_five(self):
        self.page_delete()