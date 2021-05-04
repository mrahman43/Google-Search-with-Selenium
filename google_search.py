from selenium import webdriver
import pandas as pd
import unittest


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_search_something(self):
        self.excel_file = pd.read_excel('./search_file.xlsx')
        self.search_value = self.excel_file._get_value(0,'Test Data')
        self.driver.get('https://www.google.com/')
        self.googleTextfield = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        self.googleTextfield.send_keys(self.search_value)
        self.googleTextfield.submit()
        self.driver.implicitly_wait(10)

        self.findadd = self.driver.find_element_by_css_selector('#center_col a:first-child')
        if ((self.findadd.is_displayed()) == True):
            self.findadd.click()
        else:
            self.driver.find_element_by_css_selector('#search a:first-child').click()
        self.driver.implicitly_wait(10)




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test complete")


if __name__ == '__main__':
    unittest.main()
