from selenium import webdriver

class GetDriver(object):
    #初始化浏览器
    driver=None

    #获取浏览器
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver=webdriver.Chrome()
            cls.driver.get('http://localhost/index.php')
            cls.driver.maximize_window()
        return cls.driver
    #退出浏览器
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None

