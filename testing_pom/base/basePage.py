from selenium import webdriver
import time
#打开浏览器
class BasePage:
    # 初始化浏览器
    def __init__(self, driver):
        self.driver = driver
    def open_browse(self,url):
        #获取url
        self.driver.get(url)
        #窗口最大化
        self.driver.maximize_window()
        #等待10秒钟
        self.driver.implicitly_wait(10)
        return self.driver
    # 定位元素
    def locator(self, loc):
        return self.driver.find_element(*loc)
    #输入文字
    def input_text(self,loc,text):
            self.locator(loc).send_keys(text)
    #点击元素
    def click(self, loc):
        self.locator(loc).click()



    #等待
    def wait(self,scd):
        time.sleep(scd)
    #关闭浏览器
    def quit(self):
        self.driver.quit()
# if __name__ == '__main__':
#     driver = open_browse('Chrome','https://www.baidu.com')
#     WebUi.input_text('id','kw','bbt')
#     WebUi.click('id','su')
#     WebUi.closs_browse()