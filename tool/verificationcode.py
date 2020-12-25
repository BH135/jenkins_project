from selenium import webdriver
from PIL import Image
import base64
import json
import requests
from base.get_driver import GetDriver
from page.page_knowledgebase import KnowledgeBase


class Know():

    def __init__(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化 PageKnowledgeBase页面
        self.kb = KnowledgeBase(self.driver)

    def screen_shot(self):
        self.driver.save_screenshot(r"D:\zhuce.png") # 截下当前页面的图
        left_angle = self.driver.find_element_by_class_name("imgcode").location # 获取验证码左上角坐标
        print(left_angle) # 查看验证码图片左上角点的坐标
        left = left_angle["x"] # 获取验证码图片最左边的x轴坐标
        top = left_angle["y"] # 获取验证码图片最上面的y轴坐标
        image = self.driver.find_element_by_class_name("imgcode") # 对整个图片进行定位
        width = image.size["width"] # 获取图片的宽度
        height = image.size["height"] # 获取图片的高度
        right = left+width # 获取验证码图片最右边的x轴坐标
        down = top+height # 获取验证码图片最下面的y轴坐标
        print(left,top,right,down) # 打印四个角的横纵坐标

        openim = Image.open(r"D:\zhuce.png") #打开刚才截下的整个的图片
        jietu = openim.crop((left,top,right,down)) #通过刚才获得的四个坐标进行截图（Imagez中的方法） 这里是两个小括号
        jietu.save(r"D:\xi.png") #截取验证码的小图并继续保存

    def base64_api(self,uname, pwd, typeid, img):
        with open(img, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            b64 = base64_data.decode()
        data = {"username": uname, "password": pwd, "typeid":typeid, "image": b64}
        result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]
        return ""

if __name__=="__main__":
    Know().screen_shot()
    img_path = "D:/xi.png"
    result = Know().base64_api(uname='python_t', pwd='bh801300', typeid="11", img=img_path)
    print(result)
