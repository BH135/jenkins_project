from selenium import webdriver
import pprint,time
import unittest
from BeautifulReport import BeautifulReport
import os


class LSSZ(unittest.TestCase):
    def save_img(self,imgName):
        filename = os.path.dirname(os.path.dirname(__file__))+"/img/"
        #截图
        self.driver.get_screenshot_as_file("{}/{}.png".format(filename,imgName))
    @classmethod
    def setUpClass(self):
        #打开谷歌浏览器
        self.driver = webdriver.Chrome()
        #将浏览器窗口最大化
        self.driver.maximize_window()
        #输入cookie记录URL
        self.driver.get("http://113.128.179.250:8020/tydt-cim/index")
        # 输入有效用户名
        self.driver.find_element_by_name("username").send_keys("admin")
        # 输入正确的密码
        self.driver.find_element_by_name("password").send_keys("tydt_123456")
        # 等待20秒
        time.sleep(5)
        self.driver.find_element_by_id('btnSubmit').click() #登录系统
        time.sleep(3)  # 等待3秒
        self.driver.find_element_by_xpath('//*[@id="cim"]').click()  # 进入绿色城市平台
        time.sleep(3)
        print(self.driver.current_url)  # 打印当前的url
        hand = self.driver.window_handles  # 获取当前的所有句柄
        print(hand)  # 打印当前的所有句柄
        self.driver.switch_to.window(hand[1])  # 转换窗口至最高的句柄
        result_url = self.driver.current_url  # 获取当前句柄之后的url
        print(self.driver.current_url)  #打印当前句柄之后的url)
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_01_PolicyManagement(self):
        self.driver.find_element_by_xpath('//*[@id="2076"]').click() #进入知识库管理页面
        time.sleep(1) #等待1秒
        iframe = self.driver.find_element_by_id('frmright') # 切换进入iframe页面
        self.driver.switch_to.frame(iframe)

        self.driver.find_element_by_xpath('//*[@id="document-content"]/dl/div/dd[4]/span/div/label').click()

        time.sleep(2)
        self.driver.find_element_by_class_name("other-move").click()


        time.sleep(5)
        iframe = self.driver.find_element_by_name('layui-layer-iframe1')  # 切换进入iframe页面
        self.driver.switch_to.frame(iframe)

        time.sleep(5)
        self.driver.find_element_by_id("tree_4_a").click()

        self.driver.switch_to.default_content()

        iframe = self.driver.find_element_by_id('frmright')  # 切换进入iframe页面
        self.driver.switch_to.frame(iframe)

        self.driver.find_element_by_class_name("layui-layer-btn0").click()
