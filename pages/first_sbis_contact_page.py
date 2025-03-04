import allure
from selenium.webdriver.support.wait import WebDriverWait
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class FirstContactSectionPage(BasePage):

    PAGE_URL = Links.HOST

    CONTACT = ("xpath", "//*[contains(@class, 'sbisru-Header__menu-link') and contains(@class, 'sbis_ru-Header__menu-link')]")
    MORE_OFFICES = ("xpath", "//span[contains(text(), 'Еще') and contains(text(), 'офис')]")
    BANNER_TENZOR = ("xpath", "(//img[@alt='Разработчик системы Saby — компания «Тензор»'])[1]")
    STRENGTH_PEOPLE = ("xpath", "(//p[contains(@class, 'tensor_ru-Index__card-title')])[2]")
    MORE_LINK = ("xpath", "(//a[contains(@class, 'tensor_ru-link') and contains(@class, 'tensor_ru-Index__link')])[2]")
    ALL_IMAGES = ("xpath", "//div[contains(@class, 'tensor_ru-About__block3-image-filter')]")

    @allure.step("Enter contact section")
    def enter_contact_section(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTACT)).click()

    @allure.step("Enter more offices")
    def enter_more_offices(self):
        self.wait.until(EC.element_to_be_clickable(self.MORE_OFFICES)).click()

    @allure.step("Enter banner tenzor")
    def enter_banner_tenzor(self):
        self.wait.until(EC.presence_of_element_located(self.BANNER_TENZOR))
        banner = self.wait.until(EC.element_to_be_clickable(self.BANNER_TENZOR))
        banner.click()

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Block visible")
    def people_block_visible(self):
        element_strength_people = self.wait.until(EC.presence_of_element_located(self.STRENGTH_PEOPLE))
        return element_strength_people.is_displayed()

    @allure.step("Enter click more link")
    def click_more_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MORE_LINK)).click()

    @allure.step("Check same size")
    def same_size(self):
        images = self.driver.find_elements(*self.ALL_IMAGES)
        sizes = [(img.size['width'], img.size['height']) for img in images]
        return all(size == sizes[0] for size in sizes)



