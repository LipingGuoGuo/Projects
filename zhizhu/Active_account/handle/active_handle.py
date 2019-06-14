from page.active_page import ActivePage

class ActiveHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.active_p = ActivePage(self.driver)

    # 输入知号
    def send_knowledge_number(self, number):
        self.active_p.get_knowledge_number_element().send_keys(number)

    # 输入密码
    def send_password(self, password):
        self.active_p.get_password_element().send_keys(password)

    # 获取文字信息
    def get_user_text(self,info):
        try:
            if info == "knowledge_number_error":
                text = self.active_p.get_knowledge_number_error_element().text
            else:
                text = self.active_p.get_password_error_element().text
        except:
            text = None
        return text

    # 点击登录按钮
    def click_active_button(self):
        self.active_p.get_button_element().click()

    #


