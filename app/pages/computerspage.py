from app.selectors.computers import Computers
from playwright.async_api import Page
from app.core.logger import logger

class ComputersPage:
    def __init__(self, page: Page) -> None:
        logger.info(__name__)
        self.page = page
        self.selectors = Computers()

    async def add_new_computer(self):
        logger.info(__name__)
        await self.page.locator(self.selectors.add_new_computer).click()
