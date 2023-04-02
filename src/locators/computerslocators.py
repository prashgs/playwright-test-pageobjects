from playwright.sync_api import Page, Locator
from src.core.elementtypes import Button, GenericElement, TextInput


class ComputersLocators:
    __search_box_selector = '#searchbox'
    __filter_by_name = '#searchsubmit'
    __add_new_computer_selector = '#add'
    __alert_message = '.alert-message.alert-message'

    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def search_box(self):
        return TextInput(self.page, selector=self.__search_box_selector)

    @property
    def add_new_computer(self):
        return Button(self.page, selector=self.__add_new_computer_selector)

    @property
    def alert_message(self):
        return GenericElement(self.page, selector=self.__alert_message)
