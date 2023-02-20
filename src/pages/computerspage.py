from src.selectors.computers import Computers
from playwright.sync_api import Page
from src.core.logger import logger


class ComputersPage:
    def __init__(self, page: Page) -> None:
        logger.info(__name__)
        self.page = page
        self.locators = Computers(self.page)

    def add_new_computer(self):
        logger.info(__name__)
        self.locators.add_new_computer.click_element()
