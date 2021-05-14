import pytest
import yaml
from selenium import webdriver
import os
from testing_pom.page_object.login_page import LoginPage
from testing_pom.page_object.search_page import SearchPage
from testing_pom.config.yamlload import loadyaml


class TestCase:

    def setup_class(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.lg = LoginPage(self.driver)
        self.sc = SearchPage(self.driver)
        print('打开浏览器')

    def teardown_class(self):
        # 关闭浏览器
        self.driver.quit()
        print('关闭浏览器')

    # 测试用例
    # @pytest.mark.run(order=2)#指定运行顺序

    @pytest.mark.parametrize('utxt', loadyaml('./data/login.yaml'))

    def test_Login(self, utxt):
        self.lg.Login(utxt['username'], utxt['password'])
        self.lg.wait(3)

    # @pytest.mark.run(order=1)

    @pytest.mark.parametrize('god', loadyaml('./data/search.yaml'))
    def test_Search(self, god):
        self.sc.SearchGoods(god['goods'])
        # self.sc.wait(3)


if __name__ == '__main__':
    pytest.main(['-sv'])
