from base.find_element import FindElement

class ActivePage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取知号元素
    def get_knowledge_number_element(self):
        return self.fd.get_element("knowledge_number")

    # 获取密码元素
    def get_password_element(self):
        return self.fd.get_element("password")

    # 获取注册按钮元素
    def get_button_element(self):
        return self.fd.get_element("register_button")

    # 获取知号错误元素
    def get_knowledge_number_error_element(self):
        return self.fd.get_element("knowledge_number_error")

     # 获取密码错误元素
    def get_password_error_element(self):
        return self.fd.get_element("password_error")
