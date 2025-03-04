import pytest
from pages.first_sbis_contact_page import FirstContactSectionPage
from pages.second_sbis_contact_page import SecondContactSectionPage
from pages.third_download_page import ThirdBaseDownload


class BaseTest:
    first_contact_section_page = FirstContactSectionPage
    second_sbis_contact_page = SecondContactSectionPage
    third_download_page = ThirdBaseDownload


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.first_contact_section_page = FirstContactSectionPage(driver)
        request.cls.second_sbis_contact_page = SecondContactSectionPage(driver)
        request.cls.third_download_page = ThirdBaseDownload(driver)
