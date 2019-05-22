from PIL import Image
from ShowapiRequest import ShowapiRequest
import time
class GetCode:
    def __init__(self, driver):
        self.driver = driver

    # 获取图片
    def get_code_image(self, file_name):
        self.driver.save.screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop(left, top, right, height)
        img.save(file_name)
        time.sleep(2)

    # 解析图片获取验证码信息
    def code_online(self, file_name):
        r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
        r.addBodyPare("typeId", "35")
        r.addBodyPare("convert_to_jpg", "0")
        r.addFilePare("image", file_name)  # 文件上传时设置
        res = r.post()
        # print(res.text) 调试输出检查结果
        text = res.json()['showapi_res_body']['Result']
        time.sleep(2)
        return text
