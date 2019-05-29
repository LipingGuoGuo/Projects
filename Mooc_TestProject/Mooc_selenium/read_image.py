#coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest

# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
# tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'
#
# image = Image.open("F:/test.png")
# text = pytesseract.image_to_string(image, config=tessdata_dir_config)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-5", "96517", "213a7970dd72492aaaee595c9d64f7d9" )
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"F:/imooc1.png")  # 文件上传时设置
res = r.post()
# text = res.json()["showapi_res_body"]["Result"]
print(res.text)  # 返回信息