from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class Element:
    def __init__(self, page: Page, selector: str):
        self.page = page
        self.selector = selector
