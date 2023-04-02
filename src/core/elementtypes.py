

from src.core.baseelement import BaseElement
from playwright.sync_api import Page, Locator


class TextInput(BaseElement):
    """
    A page element representing a text input field.
    """

    def __init__(self, page: Page, selector: str):
        super().__init__(page, selector)

    def send_keys(self, value):
        self.__call__().fill(value=value)


class Button(BaseElement):
    """
    A page element representing a text input field.
    """

    def __init__(self, page: Page, selector: str):
        super().__init__(page, selector)
        self.locator = self.page.locator(selector=selector)

    def click_custom(self):
        self.locator.click(trial=True)
        self.locator.click()


class GenericElement(BaseElement):
    """
    A page element representing a text input field.
    """

    def __init__(self, page: Page, selector: str):
        super().__init__(page, selector)

    # def __call__(self) -> Locator:
    #     return self.page.locator(self.selector)
