from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
driver = webdriver.Chrome()

# 浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

# 获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample("1234567890abcdefghijklmn", 8))
    return user_info

# 获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
    print(code_element.location)
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop(left, top, right, height)
    img.save(file_name)

# 解析图片获取验证码信息
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-5", "96517", "213a7970dd72492aaaee595c9d64f7d9")
    r.addBodyPara("img_base64",
                  "data:image/jpeg;base64,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")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    r.addFilePara("image", file_name)  # 文件上传时设置
    res = r.post()
    text = res.json()["showapi_res_body"]["Result"]
    return text

# 运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info + "@163.com"
    file_name = "E:/Image/test02.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys()
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register_btn").click()
    driver.close()

run_main()

