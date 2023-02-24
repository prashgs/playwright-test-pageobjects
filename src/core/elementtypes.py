

from src.core.baseelement import BaseElement
from playwright.sync_api import Page, Locator


class TextInput(BaseElement):
    """
    A page element representing a text input field.
    """

    def __init__(self, page: Page, selector: str):
        super().__init__(page, selector)

    def send_keys(self, value):
        element = self.page.locator(self.selector)
        element.fill(value=value)




class Button(BaseElement):
    """
    A page element representing a text input field.
    """

    def __init__(self, page: Page, selector: str):
        super().__init__(page, selector)

    def click_element(self):
        element = self.page.locator(self.selector)
        element.click()


class GenericElement(BaseElement):
    """
    A page element representing a text input field.
    """

    def __init__(self, page: Page, selector: str):
        super().__init__(page, selector)

    # def __call__(self) -> Locator:
    #     return self.page.locator(self.selector)
