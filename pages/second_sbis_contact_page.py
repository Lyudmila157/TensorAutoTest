import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SecondContactSectionPage(BasePage):

    PAGE_URL = Links.HOST

    CONTACT_AREA = ("xpath", "//*[contains(@class, 'sbisru-Header__menu-link') and contains(@class, 'sbis_ru-Header__menu-link')]")
    REGION_LOCATOR = ("xpath", "(//span[contains(@class, 'sbis_ru-Region-Chooser__text') and contains(@class, 'sbis_ru-link')])[1]")
    MORE_OFFICE = ("xpath", "//span[contains(text(), 'Еще') and contains(text(), 'офис')]")
    MY_REGION = ("xpath", "(//span[contains(@class, 'sbis_ru-Region-Chooser__text') and contains(@class, 'sbis_ru-link')])[1]")
    PARTNERS = ("xpath", "//div[contains(@class, 'sbisru-Contacts-List__name')]")
    REGION_KAMCHATKA = ("xpath", "//span[@title='Камчатский край' and contains(@class, 'sbis_ru-link')]")
    CHANGE_REGION = ("xpath", "(//span[contains(@class, 'sbis_ru-Region-Chooser__text') and contains(@class, 'sbis_ru-link')])[1]")
    PARTNER_KAMCHATKA = ("xpath", "//div[contains(@title, 'Saby - Камчатка')]")

    @allure.step("Enter second contact section")
    def enter_second_contact_section(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTACT_AREA)).click()

    @allure.step("Region present")
    def region_present(self):
        return self.wait.until(EC.presence_of_element_located(self.REGION_LOCATOR)).text

    @allure.step("Enter more office")
    def enter_more_office(self):
        self.wait.until(EC.element_to_be_clickable(self.MORE_OFFICE)).click()

    @allure.step("Check my region")
    def check_my_region(self):
        return self.wait.until(EC.presence_of_element_located(self.MY_REGION)).text

    @allure.step("Partners in region")
    def partners_in_region(self):
        partners = self.wait.until(EC.presence_of_all_elements_located(self.PARTNERS))
        return [partner.text for partner in partners]

    @allure.step("CLick region")
    def click_region(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_REGION)).click()

    @allure.step("Select Kamchatka region")
    def select_kamchatka_region(self):
        self.wait.until(EC.element_to_be_clickable(self.REGION_KAMCHATKA)).click()

    @allure.step("Check selected region")
    def check_selected_region(self):
        self.wait.until(EC.text_to_be_present_in_element(self.CHANGE_REGION, "Камчатский край"))
        return self.wait.until(EC.presence_of_element_located(self.CHANGE_REGION)).text

    @allure.step("Check partner in Kamchatka region")
    def check_partner_in_kamchatka(self):
        self.wait.until(EC.presence_of_element_located(self.PARTNER_KAMCHATKA))

    @allure.step("Check Kamchatka in URL")
    def check_url_contains_kamchatka(self):
        return "kamchatskij-kraj" in self.driver.current_url

    @allure.step("Check Kamchatka in title")
    def check_title_contains_kamchatka(self):
        return "Камчатский край" in self.driver.title
