import os
import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from tool.get_logger import GetLogger

log = GetLogger().get_logger()

class Base:

    def __init__(self,driver):
        log.info("正在获取初始化driver对象: {}".format(driver))
        self.driver = driver

    # 查找元素方法 封装
    def base_find(self, loc,  timeout=30, poll=0.5):
        log.info("正在定位: {} 元素，默认定位超时时间为：{}".format(loc, timeout))
        # 使用显示等待 查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击元素 方法封装
    def base_click(self, loc):
        log.info("正在对:{} 元素实行点击事件".format(loc))
        self.base_find(loc).click()

    # 输入元素 方法封装
    def base_input(self, loc, value):
        log.info("正在给元素{} 输入内容: {}".format(loc, value))
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        log.info("正在给元素: {} 清空".format(loc))
        # 输入
        el.send_keys(value)
        log.info("正在给元素: {} 输入内容".format(loc))

    # 获取文本信息 方法封装
    def base_get_text(self, loc):
        log.info("正在获取元素: {} 文本值".format(loc))
        return self.base_find(loc).text

    # 截图 方法封装
    def base_get_image(self):
        allure.attach(self.driver.get_screenshot_as_png(), '截图', allure.attachment_type.PNG)

    # 截图 断言方法封装
    def base_get_image1(self):
        log.info("断言出错，调用截图")
        allure.attach(self.driver.get_screenshot_as_png(), '截图', allure.attachment_type.PNG)

    # 判断元素是否存在 方法封装
    def base_element_is_exist(self, loc):
        try:
            self.base_find(loc, timeout=2)
            log.info("正在判断元素: {} 存在! ".format(loc))
            return True # 代表元素存在
        except:
            log.info("正在判断元素: {} 不存在! ".format(loc))
            return False # 代表元素不存在

    # 切换窗口方法
    def base_switch_to_window(self, title):
        log.info("正在执行切换title值为: {}窗口".format(title))
        self.base_get_title_handle(title)

    # 获取指定title页面的handle方法
    def base_get_title_handle(self, title):
        # 获取当前所有页面的handles
        for handle in self.driver.window_handles:
            log.info("正在遍历handles：{}-->{}".format(handle, self.driver.window_handles))
            # 切换 handle
            self.driver.switch_to.window(handle)
            log.info("切换 :{} 窗口".format(handle))
            # 获取当前页面title 并判断 是否等于 指定参数的title
            log.info("判断当前页面title：{} 是否等于指定的title：{}".format(self.driver.title, title))
            if self.driver.title == title:
                log.info("条件成立! 返回当前handle{}".format(handle))
                # 返回 handle
                return handle

    # 切换iframe表单方法
    def base_switch_frame(self, name):
        log.info("正在获取frame: {} 元素".format(name))
        self.driver.switch_to.frame(name)

    # 封装上传文件操作
    def base_uploadfiles(self, file_path = "E:\城市项目.xlsx"):
        log.info("正在上传文件: {} ".format(file_path))
        os.system(r"E:\upfile.exe %s" % file_path)

    # 退出iframe表单方法
    def base_signout_switch_frame(self):
        log.info("正在退出frame表单: {} ".format(self.driver.switch_to.default_content))
        self.driver.switch_to.default_content()

