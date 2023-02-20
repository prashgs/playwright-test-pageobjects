from abc import ABC
from playwright.sync_api import Page


class BasePage(ABC):
    """
    An abstract base class for page elements using the Selenium Page Objects model in Python.
    """

    def __init__(self, page: Page):
        self.page = page
