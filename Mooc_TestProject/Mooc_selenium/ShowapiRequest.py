import requests
from urllib import parse

files = {}
headers = {}
body = {}
timeouts = {}
resHeader = {}

class ShowapiRequests:
    def __init__(self, url, my_appId, my_appSecret):
        self.url = url
        self.my_appId = my_appId
        self.my_appSecret = my_appSecret
        body["showapi_appid"] = my_appId
        body["showapi_sign"] = my_appSecret
        headers["User-Agent"] = ""

    def addFilePara(self, key, value_url):
        files[key] = open(r"%s" % (value_url), 'rb')
        return self

    def addHeadPara(self, key_value):


     def setTimeout(self, connecttimeout, readtimeout):
        timeouts["connecttimeout"] = connecttimeout
        timeouts["readtimeout"] = readtimeout
        return self

    def get(self):
        get_url = self.url + "?" + parse.urlencode(body)
        if not timeouts:
            res = requests.get(get_url, headers=headers)
        else:
            timeout = (timeouts["connecttimeout"], timeouts["readtimeout"])
            res = requests.get(get_url, headers = headers, timeouts = timeouts)
        return res

    def post(self):
        if not timeouts:
            res = requests.post(self.url, files = files, data=body, headers = headers)
        else:
            timeout = (timeouts["connecttimeout"], timeouts["readtimeout"])
