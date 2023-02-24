from playwright.sync_api import Page, Locator
from src.core.elementtypes import GenericElement, TextInput


class ComputersLocators:
    __search_box_selector = '#searchbox'
    __filter_by_name = '#searchsubmit'
    __add_new_computer_selector = '#add'
    __alert_message = '.alert-message.alert-message'

    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def search_box(self) -> Locator:
        locator = TextInput(self.page, selector=self.__search_box_selector)
        return locator()

    @property
    def add_new_computer(self) -> Locator:
        locator = TextInput(
            self.page, selector=self.__add_new_computer_selector)
        return locator()

    @property
    def alert_message(self) -> Locator:
        locator = GenericElement(self.page, selector=self.__alert_message)
        return locator()
