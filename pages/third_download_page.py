import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import os


class ThirdBaseDownload(BasePage):

    PAGE_URL = Links.HOST

    LOCAL_DOWNLOAD = ("xpath", "//a[contains(@class, 'sbisru-Footer__link') and contains(text(), 'Скачать локальные версии')]")
    SABY_PLUGIN = ("xpath", "(//div[contains(@class, 'controls-TabButton__caption')])[1]")
    INSTALLER = ("xpath", "(//a[contains(@class, 'sbis_ru-DownloadNew-loadLink__link')])[1]")

    @allure.step("Click on local download")
    def click_on_local_download(self):
        self.wait.until(EC.element_to_be_clickable(self.LOCAL_DOWNLOAD)).click()

    @allure.step("Click on saby plugin")
    def click_on_saby_plugin(self):
        self.wait.until(EC.element_to_be_clickable(self.SABY_PLUGIN)).click()

    @allure.step("Click on installer")
    def click_on_installer(self):
        self.wait.until(EC.element_to_be_clickable(self.INSTALLER)).click()
