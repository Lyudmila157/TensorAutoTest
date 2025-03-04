import allure
from base.base_test import BaseTest
import time
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@allure.feature("Installer Functionality")
class TestThirdDownload(BaseTest):

    @allure.title("Download")
    @allure.severity("Minor")
    def test_download(self):
        download_path = os.path.join(os.getcwd(), "tests", "downloads")
        file_name = "sbisplugin-setup-web.exe"
        downloaded_file = os.path.join(download_path, file_name)

        logger.info("Opening page for downloading plugin")
        self.third_download_page.open()

        logger.info("Click on link 'Download local versions'")
        self.third_download_page.click_on_local_download()

        logger.info("Click on link 'Download SBIS Plugin'")
        self.third_download_page.click_on_saby_plugin()

        logger.info("Click on button to install plugin")
        self.third_download_page.click_on_installer()

        logger.info("Waiting for file download to complete")
        time.sleep(10)
        if os.path.exists(downloaded_file):
            logger.info(f"File downloaded successfully: {downloaded_file}")
        else:
            logger.error(f"File not found on path: {downloaded_file}")
        print(f"File downloaded here: {downloaded_file}")
