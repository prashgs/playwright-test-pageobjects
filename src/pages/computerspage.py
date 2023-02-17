from src.selectors.computers import Computers
from playwright.sync_api import Page
from src.core.logger import logger


class ComputersPage:
    def __init__(self, page: Page) -> None:
        logger.info(__name__)
        self.page = page
        self.selectors = Computers()

    def add_new_computer(self):
        logger.info(__name__)
        self.page.locator(self.selectors.add_new_computer).click()
