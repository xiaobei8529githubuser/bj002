from base.base import Base
import page

class PageLogin(Base):

    #首页登录
    def page_click_login_link(self):
        self.base_click(page.login_link)

    #输入用户名
    def page_input_username(self,username):
        self.base_input(page.login_username,username)

    #输入密码
    def page_input_password(self,pwd):
        self.base_input(page.login_pwd,pwd)

    #输入验证码
    def page_input_code(self,code):
        self.base_input(page.login_verify_code,code)

    #点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    #获取异常提示信息
    def page_get_err_info(self):
        return self.base_get_text(page.login_err_info)
    #点击异常提示框确定按钮
    def page_click_err_ok_btn(self):
        self.base_click(page.login_err_btn)


    #获取登录后的昵称
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    #安全退出
    def page_click_logout(self):
        self.base_click(page.login_logout)
    #登录业务实现
    def page_login_tpshop(self,username,pwd,code):
        # self.page_click_index_login()
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_input_code(code)
        self.page_click_login_btn()

