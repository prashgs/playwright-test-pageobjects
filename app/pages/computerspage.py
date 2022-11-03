from app.locators.computers import Computers
from playwright.async_api import Page


class ComputersPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.selectors = Computers()

    async def add_new_computer(self):
        await self.page.locator(self.selectors.add_new_computer).click()
