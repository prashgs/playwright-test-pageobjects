from playwright.sync_api import Page


class BaseElement:

    def __init__(self, page: Page, selector: str):
        self.page = page
        self.selector = selector
