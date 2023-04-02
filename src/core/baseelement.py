from playwright.sync_api import Page, Locator
from abc import abstractmethod

class BaseElement:

    def __init__(self, page: Page, selector: str):
        self.page = page
        self.selector = selector

    def __call__(self) -> Locator:
        return self.page.locator(self.selector)

    @abstractmethod
    def click_custom(self):
        return
