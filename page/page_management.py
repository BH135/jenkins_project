from time import sleep

import allure

import page
from base.base import Base
from tool.get_logger import GetLogger

log = GetLogger().get_logger()

class Management(Base):

    @allure.step(title='点击CIM跳转至绿色数字城市CIM基础平台')
    def page_cim(self):
        sleep(2)
        self.base_click(page.currency_cim)

    # 资料管理
    @allure.step(title='点击资料管理')
    def page_click_management(self):
        # 切换句柄
        self.base_switch_to_window(page.pay_my_prder_title)
        # 点击资料管理
        self.base_click(page.management)
        # 截图
        self.base_get_image()

    # 文件夹新增测试
    @allure.step(title='文件夹增加测试')
    def page_folder(self, value = "测试"):
        # 切换frame表单
        self.base_switch_frame(page.currency_frame_name)
        # 点击新建文件夹
        self.base_click(page.management_new_folder)
        # 切换frame表单
        self.base_switch_frame(page.currency_frame_name1)
        # 输入文件夹名称
        self.base_input(page.management_foldername, value)
        # 退出frame表单
        self.base_signout_switch_frame()
        # 切换frame表单
        self.base_switch_frame(page.currency_frame_name)
        # 点击确定
        self.base_click(page.management_determine)
        # 截图
        self.base_get_image()

    # 获取业务新增结果
    def page_get_text_new(self):
        # 获取结果并返回
        log.info("正在获取业务新增结果: {} ".format(page.management_folder_results))
        sleep(2)
        return self.base_get_text(page.management_folder_results)

    # 文件上传测试
    @allure.step(title='文件上传测试')
    def page_file(self):
        # 点击上传
        self.base_click(page.management_upload)
        # 开始上传文件
        sleep(3)
        self.base_uploadfiles()
        # 截图
        self.base_get_image()

    # 获取上传文件结果
    def page_get_file(self):
        # 获取结果并返回
        log.info("正在获取上传结果: {} ".format(self.base_get_text(page.management_upload_results)))
        sleep(2)
        return self.base_get_text(page.management_upload_results)

    # 文件移动测试
    @allure.step(title='文件移动测试')
    def page_file_move(self):
        # 选择要移动的文件
        self.base_click(page.management_option_box)
        # 点击移动
        sleep(5)
        self.base_click(page.management_move)
        # 切换frame-1表单
        sleep(5)
        log.info("正在切换frame: {} ".format(self.base_switch_frame(page.currency_frame_name1)))
        self.base_switch_frame(page.currency_frame_name1)
        # 选择要移动的文件夹
        self.base_click(page.management_move_folder)
        # 退出frame表单
        self.base_signout_switch_frame()
        # 切换frame-0表单
        self.base_switch_frame(page.currency_frame_name)
        # 点击确定
        self.base_click(page.management_determine)
        # 点击测试文件夹
        self.base_click(page.management_test_folder)
        # 截图
        self.base_get_image()

    # 获取业务移动结果
    def page_move_results(self):
        # 获取结果并返回
        sleep(2)
        return self.base_get_text(page.management_move_folder)



    # 组合业务方法-01
    def page_management_one(self):
        self.page_cim()
        self.page_click_management()
        self.page_folder()
        self.page_get_text_new()

    # 组合业务方法-02
    def page_management_tow(self):
        self.page_file()
        self.page_get_file()

    # 组合业务方法-03
    def page_management_three(self):
        self.page_file_move()
        self.page_move_results()





