import allure
from base.base_test import BaseTest
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@allure.feature("Contact Functionality")
class TestContactFlow(BaseTest):

    @allure.title("Click contact")
    @allure.severity("Critical")
    def test_contact_section(self):
        logger.info("Opening contact section page")
        self.first_contact_section_page.open()

        logger.info("Entering contact section")
        self.first_contact_section_page.enter_contact_section()

        logger.info("Entering more offices")
        self.first_contact_section_page.enter_more_offices()

        logger.info("Entering banner tensor")
        self.first_contact_section_page.enter_banner_tenzor()

        assert "tensor.ru" in self.first_contact_section_page.driver.current_url, "Not moved to Tensor!"
        logger.info("Successfully navigated to Tensor page")
        print("Tensor page successfully opened!")

        assert self.first_contact_section_page.people_block_visible(), "'Strength in people' block not found!"
        logger.info("'Сила в людях' block is visible")

        self.first_contact_section_page.click_more_link()
        assert "about" in self.first_contact_section_page.driver.current_url, "not moved to section'О нас'!"
        logger.info("Navigated to 'About' section")

        assert self.first_contact_section_page.same_size(), "Images are different sizes!"
        logger.info("Verified that all images have the same size")



