from selenium import webdriver
from testing_pom.base.basePage import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    url = "http://www.xn--doqq5ob5s2ut.com/index.php"
    search = (By.XPATH, '//*[@id="keyword"]')
    searchBtn = (By.XPATH, '//*[@id="searchForm"]/input[2]')

    # addCart = (By.XPATH, '//*[@id="body"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[1]/dl/dd[2]/a')
    def SearchGoods(self, goods):
        self.open_browse(self.url)
        self.input_text(self.search, goods)
        self.click(self.searchBtn)
        # self.wait(3)
        self.quit()

        # self.click(self.addCart)


if __name__ == '__main__':
    driver = SearchPage(webdriver.Chrome())
    driver.SearchGoods('人参')
