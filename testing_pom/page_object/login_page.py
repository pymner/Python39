from selenium import webdriver
from testing_pom.base.basePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    url = "http://www.xn--doqq5ob5s2ut.com/member.php?act=login&from=L2luZGV4LnBocA=="
    # 登录
    # login=(By.CSS_SELECTOR,'#body > div.qikoo-top-box > div.top-bar.js_top_bar > div > div.top-user-box > div.fl.login-box > div.text-lnk.jsLogin')
    # 账户登录
    # zlogin=(By.XPATH,'//*[@id="body"]/div[12]/div[1]/div/div/div/div[2]/a')
    # 用户名
    username = (By.NAME, 'username')
    # 密码
    password = (By.NAME, 'password')
    # 登录按钮
    LoginBt = (By.NAME, 'imageField')

    # 登录
    def Login(self, usne, pwd):
        self.open_browse(self.url)
        # self.click(self.login)
        # self.click(self.zlogin)
        # 输入用户名
        self.input_text(self.username, usne)
        # 输入密码
        self.input_text(self.password, pwd)
        # 点击登录
        self.click(self.LoginBt)
        # self.wait()


if __name__ == '__main__':
    driver = LoginPage(webdriver.Chrome())
    driver.Login('15631223581', 'hu111111')
