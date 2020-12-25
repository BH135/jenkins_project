import allure
import page
from base.base import Base
from time import sleep
from tool.verificationcode import Know
from tool.get_logger import GetLogger

log = GetLogger().get_logger()

class PageLogin(Base,Know):
    # 点击登录链接
    # def page_click_login_link(self):
    #     self.base_click(page.login_link)

    # 输入用户名
    @allure.step(title='输入用户名')
    def page_input_username(self, username):
        log.info("[page_loging] 对：{} 元素 输入用户名：{} 操作".format(page.login_username ,username))
        self.base_input(page.login_username ,username)

    # 输入密码
    @allure.step(title='输入密码')
    def page_input_password(self, pwd):
        log.info("[page_loging] 对：{} 元素 输入密码：{} 操作".format(page.login_pwd, pwd))
        self.base_input(page.login_pwd, pwd)

    # 对验证码进行调用截图操作
    def page_screenshot(self):
        log.info("[page_loging] 对：{} 进行截图操作".format(self.screen_shot()))
        self.screen_shot()

    # 输入验证码
    @allure.step(title='输入验证码')
    def page_input_verify_code(self, img_path = "D:/xi.png"):
        return1 = self.base64_api(uname='python_t', pwd='bh801300', typeid="11", img=img_path)
        log.info("[page_loging] 对：{} 元素 输入验证码：{}".format(page.login_verify_code, return1))
        BL = page.login_verify_code
        for i in page.login_verify_code:
            if page.login_verify_code == BL:
                self.base_input(page.login_verify_code, return1)
            else:
                self.base_input(page.login_verify_code, return1)
                self.page_click_login_bth()

    # 点击登录按钮
    @allure.step(title='点击登录')
    def page_click_login_bth(self):
        self.base_click(page.login_btn)

    # 判断是否登录成功
    def page_get_error_info(self):
        return self.base_get_text(page.login_err_info)

    # 点击异常信息框 确定
    # def page_click_err_bth_ok(self):
    #     self.base_click(page.login_err_btn_ok)

    # 截图
    @allure.step(title='截图')
    def page_get_img(self):
        self.base_get_image()

    #组合业务方法
    def page_login(self,username="admin",pwd="tydt_123456"):
        log.info("[page_loging] 正在执行登陆操作，用户名：{} 密码：{}".format(username,pwd))

        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_screenshot()
        self.page_input_verify_code()
        self.page_click_login_bth()