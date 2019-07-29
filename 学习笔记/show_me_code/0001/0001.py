# 第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
# random模块：生成随机数
# PIL模块：图像处理模块
# Image：载入图片
# ImageFont：载入字体
# ImageDraw：创建图片对象
from PIL import Image, ImageDraw, ImageFont
import random

# 生成随机数
msgNum = str(random.randint(1, 99))

# read image
# 载入图片
im = Image.open('glp.png')
# 获取图片宽度和高度
w, h = im.size
# 定义数字坐标
wDraw = 0.8 * w
hDraw = 0.8 * w

# Draw image
# 载入数值的字体和大小
# 从window下找到字体的资源文件，并拷贝到/usr/share/fonts/目录下，然后定义font对象的时候写上字体的存放的完整路径
font = ImageFont.truetype('user/share/fonts/arialbd.ttf', 36)
# 创建图像
draw = ImageDraw.Draw(im)
# 定义图像格式：坐标，随机数，自定义字体及大小，颜色
draw.text((wDraw, hDraw), msgNum, font=font, fill=(255, 33, 33))


# Save image
# 指定格式保存生成图像
im.save('glp_msg.png', 'png')