from page.register_page import RegisterPage
from util.get_code import GetCode
class LoginHandle(object):
    def __init__(self):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)
    # 输入邮箱
    def send_user_email(self, email):
        # email_element 获取的是页面邮箱元素
        self.register_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_name(self, username):
        self.register_p.get_username_element().send_keys(username)

    # 输入密码
    def send_user_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_user_code(self, filename):
        get_code_text = GetCode(self, driver)
        code = get_code_text.code_online(filename)
        self.register_p.get_code_element().send_keys(code)

    # 获取文字信息
    def get_user_text(self, info, user_info):
        try:
            if info == "email_error":
                text = self.register_p.get_email_error_element().text
            elif info == "name_error":
                text = self.register_p.get_email_error_element().text
            elif info == "password_error":
                text = self.register_p.get_password_error_element().text
            else:
                text = self.register_p.get_code_element().text
        except:
            text = None
        return text

    # 点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    # 获取注册按钮信息
    def get_register_text(self):
        return self.register_p.get_button_element().text