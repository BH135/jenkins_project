from time import sleep
import allure
import page
from base.base import Base
from tool.get_logger import GetLogger

log = GetLogger().get_logger()

class FileStore(Base):

    @allure.step(title='点击CIM跳转至绿色数字城市CIM基础平台')
    def page_cim(self):
        sleep(2)
        self.base_click(page.currency_cim)


    # 文件存储
    @allure.step(title='点击文件存储')
    def page_file_store(self):
        # 切换句柄
        self.base_switch_to_window(page.pay_my_prder_title)
        sleep(1)
        # 点击文件存储
        self.base_click(page.file_store)
        # 截图
        self.base_get_image()

    # 空间管理
    @allure.step(title='点击空间管理')
    def page_file_management(self):
        # 切换frame表单
        self.base_switch_frame(page.currency_frame_name)
        # 点击空间管理
        self.base_click(page.file_store_management)
        # 截图
        self.base_get_image()

    # 点击新增
    @allure.step(title='点击新增')
    def page_newly_added(self):
        self.base_click(page.file_store_newly_added)
        # 截图
        self.base_get_image()

    # 业务名称
    @allure.step(title='输入测试业务名称')
    def page_business_name(self, Spacename):
        # 切换frame表单
        self.base_switch_frame(page.currency_frame_name1)
        sleep(1)
        # 输入测试业务名称
        log.info("[page_loging] 对：{} 元素 输入名称：{} 操作".format(page.file_store_space_name, Spacename))
        self.base_input(page.file_store_space_name, Spacename)
        # 截图
        self.base_get_image()

    # 确定
    @allure.step(title='业务新增确认测试')
    def page_click_ok(self):
        # 退出frame表单
        self.base_signout_switch_frame()
        # 进入初始frame表单
        self.base_switch_frame(page.currency_frame_name)
        # 点击确定
        self.base_click(page.file_store_ok)
        # 截图
        self.base_get_image()

    # 获取业务新增结果
    def page_get_text_new(self):
        # 获取结果并返回
        sleep(2)
        return self.base_get_text(page.file_store_new_results)

    # 文件上传测试
    @allure.step(title='文件上传测试')
    def page_file(self):
        # 点击文件
        self.base_click(page.file_store_file)
        # 点击上传
        self.base_click(page.file_store_upload)
        # 开始上传文件
        sleep(3)
        self.base_uploadfiles()
        # 截图
        self.base_get_image()

    # 获取上传文件结果
    def page_get_file(self):
        # 获取结果并返回
        sleep(2)
        log.info("[page_loging] 正在获取上传结果：{}".format(self.base_get_text(page.file_store_upload_results)))
        return self.base_get_text(page.file_store_upload_results)

    # 删除测试数据
    @allure.step(title='删除测试数据')
    def page_delete(self):
        # 点击删除文件
        self.base_click(page.file_store_file_deletion )
        # 确认删除
        self.base_click(page.file_store_confirm_delete)
        # 点击空间管理
        self.base_click(page.file_store_management)
        # 点击删除业务
        self.base_click(page.file_store_delete)
        # 确认删除
        self.base_click(page.file_store_confirm_delete)
        # 截图
        self.base_get_image()

    # 组合业务方法-01
    def page_filestore_one(self,Spacename):
        self.page_cim()
        self.page_file_store()
        self.page_file_management()
        self.page_newly_added()
        self.page_business_name(Spacename)
        self.page_click_ok()
        self.page_get_text_new()

    # 组合业务方法-02
    def page_filestore_three(self):
        self.page_file()
        self.page_get_file()

    # 组合业务方法-03
    def page_filestore_four(self):
        self.page_delete()




