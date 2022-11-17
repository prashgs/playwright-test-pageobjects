from src.selectors.newcomputer import NewComputer
from playwright.async_api import Page
from src.core.logger import logger


class AddComputerPage:
    def __init__(self, page: Page) -> None:
        logger.info(__name__)
        self.page = page
        self.selectors = NewComputer()

    async def add(self, data):
        logger.info(__name__)
        if data.computerName:
            await self.page.locator(self.selectors.computer_name).fill(data.computerName)
        if data.introducedData:
            await self.page.locator(self.selectors.introduced_date).fill(data.introducedData)
        if data.discontinuedData:
            await self.page.locator(self.selectors.discontinued_date).fill(data.discontinuedData)
        if data.company:
            await self.page.locator(self.selectors.select_company).select_option(label=data.company)

    async def create_computer(self):
        logger.info(__name__)
        await self.page.locator(self.selectors.create_computer).click()
