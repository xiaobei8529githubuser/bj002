import os
import sys
from time import sleep

sys.path.append(os.getcwd())

import pytest
from tools.read_txt import read_txt
from page.page_login import PageLogin
from tools.get_driver import GetDriver


def get_data():
    # return [('13888888888', '123456', '8888'), ('13800008888', '123456', '8888'), ('13888888888', '12345', '8888')]
    arrs = []
    for arr in read_txt():
        arrs.append(tuple(arr.strip().split(",")))
    return (arrs[1::])

class TestLogin():
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化PageLogin
        self.login = PageLogin(self.driver)
        # 点击登录链接
        self.login.page_click_login_link()

    # 结束
    def teardown_class(self):
        # 关闭deriver
        GetDriver().quit_driver()

    # def test_login(self,username="13888888888",pwd="123456",code="8888"):
    #     self.page.login_tpshop(username,pwd,code)

    # 测试方法
    @pytest.mark.parametrize("username,pwd,code,success,expect_result", get_data())
    def test_login(self, username, pwd, code,success,expect_result):
        # 调用业务登录方法
        self.login.page_login_tpshop(username, pwd, code)
        # 判断 正常
        if success == "true":
            try:
                # 断言 昵称
                assert expect_result==self.login.page_get_nickname()

            except Exception as e:
                self.login.base_get_img()
            finally:
                # 安全退出
                self.login.page_click_logout()
                sleep(3)
                # 点击登录链接
                self.login.page_click_login_link()

        # 否则 逆向
        else:

            # 异常提示信息
            # 点击异常提示信息确定按钮
