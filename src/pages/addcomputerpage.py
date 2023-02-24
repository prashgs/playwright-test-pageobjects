from src.core.basepage import BasePage
from src.locators.newcomputer import NewComputer
from playwright.sync_api import Page, Locator
from src.core.logger import logger


class AddComputerPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page=page)

        logger.info(__name__)
        self.page = page
        self.selectors = NewComputer()

    def add(self, data):
        logger.info(__name__)
        
        if data.computerName:
            self.page.locator(self.selectors.computer_name).fill(
                data.computerName)
        if data.introducedData:
            self.page.locator(self.selectors.introduced_date).fill(
                data.introducedData)
        if data.discontinuedData:
            self.page.locator(self.selectors.discontinued_date).fill(
                data.discontinuedData)
        if data.company:
            self.page.locator(self.selectors.select_company).select_option(
                label=data.company)

    def create_computer(self):
        logger.info(__name__)
        self.page.locator(self.selectors.create_computer).click()
