import allure
from base.base_test import BaseTest
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@allure.feature("Kamchatka Functionality")
class TestSecondContactFlow(BaseTest):

    @allure.title("Click contact and Region")
    @allure.severity("Critical")
    def test_second_contact_section(self):
        logger.info("Opening contact page")
        self.second_sbis_contact_page.open()

        logger.info("Moving to section of second contact")
        self.second_sbis_contact_page.enter_second_contact_section()

        logger.info("Checking for region availability")
        self.second_sbis_contact_page.region_present()

        logger.info("Going to section 'Еще офисы'")
        self.second_sbis_contact_page.enter_more_office()

        logger.info("Getting current region")
        my_region = self.second_sbis_contact_page.check_my_region()
        print(f"DEBUG: Region - {my_region}")

        assert "Татарстан" in my_region, f"Region determined incorrectly! Current: {my_region}"

        logger.info("Checking for partners in region")
        self.second_sbis_contact_page.partners_in_region()
        partners = self.second_sbis_contact_page.partners_in_region()
        assert len(partners) >= 19, "Fewer partners than expected!"

        logger.info("Select region Камчатка")
        self.second_sbis_contact_page.click_region()
        self.second_sbis_contact_page.select_kamchatka_region()

        logger.info("Checking the selected region")
        selected_region = self.second_sbis_contact_page.check_selected_region()
        print(f"DEBUG: Region - {selected_region}")
        assert "Камчатский край" in selected_region, f"Region determined incorrectly! Current: {selected_region}"

        logger.info("Checking partners for Kamchatka")
        self.second_sbis_contact_page.check_partner_in_kamchatka()

        logger.info("Checking URL and title for Kamchatka")
        assert self.second_sbis_contact_page.check_url_contains_kamchatka(), "URL does not contain Kamchatka Krai!"
        assert self.second_sbis_contact_page.check_title_contains_kamchatka(), "Title does not contain Kamchatka Krai!"