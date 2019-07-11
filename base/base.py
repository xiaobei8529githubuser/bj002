from selenium.webdriver.support.wait import WebDriverWait



class Base(object):
    def __init__(self,driver):
        self.driver=driver
    #查找元素方法
    def base_find_elements(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(
            lambda x:x.find_element(*loc))
    #输入方法
    def base_input(self,loc,value):
        #获取元素
        el=self.base_find_elements(loc)
        #清空
        el.clear()
        #输入
        el.send_keys(value)
    #点击方法
    def base_click(self,loc):
        self.base_find_elements(loc).click()
    #截图
    def base_get_img(self):
        self.driver.get_screenshot_as_file("./image/fail.png")
    #获取提示信息
    def base_get_text(self,text):
        pass
