from handle.active_handle import ActiveHandle

class ActiveBusiness(object):
    def __init__(self,driver):
        self.active_h = ActiveHandle(driver)

    def user_base(self,number,password):
        self.active_h.send_knowledge_number(number)
        self.active_h.send_password(password)
        self.active_h.click_active_button()

    # 知号错误
    def login_knowledge_number_error(self,number,password):
        self.user_base(number,password)
        if self.active_h.get_user_text("knowledge_number_error", "用户名不能为空") == None：
            return True







