import unittest

from ddt import ddt, file_data
from selenium import webdriver

from testing_pom.page_object.login_page import LoginPage
from testing_pom.page_object.search_page import SearchPage


@ddt
class TCast(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 打开浏览器
        cls.driver = webdriver.Chrome()
        cls.lg = LoginPage(cls.driver)
        cls.sc = SearchPage(cls.driver)
        print('打开浏览器')

    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭浏览器
        cls.driver.quit()
        print('关闭浏览器')

    # 测试用例
    @file_data('../data/login.yaml')
    def testLogin(self, username, password):
        self.lg.Login(username, password)
        self.lg.wait(3)

    @file_data('../data/search.yaml')
    def testSearch(self, goods):
        self.sc.SearchGoods(goods)
        self.sc.wait(3)


# def defaultTestResult(self):
# return result.TestResult()


if __name__ == '__main__':
    unittest.main()
