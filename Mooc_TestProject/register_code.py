from selenium import webdriver
import time
import random
from PIL import Image
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
    driver.save.screenshot(file_name)
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
    r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5")
    r.addBodyPare("typeId", "35")
    r.addBodyPare("convert_to_jpg", "0")
    r.addFilePare("image", file_name)  # 文件上传时设置
    res = r.post()
    # print(res.text) 调试输出检查结果
    text = res.json()['showapi_res_body']['Result']
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

