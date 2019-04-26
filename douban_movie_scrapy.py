import requests
import re
import openpyxl import workbook
from bs4 import BeautifulSoup as bs
import os
os.chdir("F:\Projects\Projects")

def getHtml(src):
    html = requests.get(src).content
    getData(html,src) # 首页链接和其他页不同，所以单独获取信息
    urls = re.findall('href = "(.*filter=?)',html) # re获取跳转链接的href
    for u in range(len(urls)-2):
