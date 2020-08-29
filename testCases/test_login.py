import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("**************Test_001_Login**************")
        self.logger.info("**************Verifying Home Page Title**************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title


        if act_title == "Your store. Login":
            self.logger.info("**************Home Page Title Test is passed**************")
            self.driver.close()
            assert True
        else:
            self.logger.error("**************Home Page Title Test is failed**************")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()

            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**************Verifying Login test**************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title_2 = self.driver.title


        if act_title_2 == "Dashboard / nopCommerce administration":
            self.logger.info("**************Login Test is passed**************")
            self.driver.close()

            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("**************Login Test is failed**************")
            self.driver.close()

            assert False


