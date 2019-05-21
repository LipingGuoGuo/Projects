"""
操作handle层
PO 模式设计业务层
"""
from handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)
    def user_base(self, email, name, password, code):
        self.register_h.send_user_email()
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()
        self.register_h.get_register_text()

    def register_success(self):
        if self.register_h.get_register_text() == None:
            return  True
        else:
            return False
    # 执行操作
    """
    正常操作不是全部执行完成，失去焦点获得判断即可
    """
    # 检验邮箱错误
    def login_email_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text("email_error", "请输入有效的电子邮件地址") == None:
            print("邮箱检验不成功")
            return True
        else:
            return False

    # 检验用户名错误
    def login_name_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text("name_error", "字符长度必须大于等于4，一个中文字算2个字符") == None:
            print("用户名检验不成功")
            return True
        else:
            return False

    # 检验密码错误
    def login_password_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text("password_error", "最少需要输入 5 个字符") == None:
            print("密码检验不成功")
            return True
        else:
            return False

    # 检验验证码错误
    def login_code_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text("code_text_error", "验证码错误") == None:
            print("验证码检验不成功")
            return True
        else:
            return False



