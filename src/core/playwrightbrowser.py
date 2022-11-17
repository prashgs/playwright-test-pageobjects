import os
import asyncio
from playwright.async_api import async_playwright
from src.core.logger import logger

class PlaywrightBrowser:

    def __init__(self, browser_type: str = 'chrome'):
        logger.info(__name__)
        self._browser_type = browser_type
        self._playwright = None
        self._instance = None
        self._page = None
        self._context = None
        self._url = None
        self.headless = False

    @property
    def browser_type(self):
        return self._browser_type

    @browser_type.setter
    def browser_type(self, value):
        self._browser_type = value

    @property
    def playwright(self):
        return self._playwright

    @playwright.setter
    def playwright(self, value):
        self._playwright = value

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    async def setup(self):
        logger.info(__name__)
        args = ['--start-maximized', '--windows-size=1920,1080']
        self.playwright = await async_playwright().start()

        if os.getenv("HEADLESS"):
            self.headless = os.getenv("HEADLESS").lower() == 'true'

        match self.browser_type.lower():
            case 'chrome':
                self.instance = await self.playwright.chromium.launch(args=args, headless=self.headless)
            case 'firefox':
                self.instance = await self.playwright.firefox.launch(args=args, headless=self.headless)
            case '':
                self.instance = await self.playwright.chromium.launch(args=args, headless=self.headless)
        self.context = await self.instance.new_context(no_viewport=True)
        self.page = await self.context.new_page()

    async def open_url(self, url: str):
        logger.info(__name__)
        if url:
            self.url = url
        await self.page.goto(url=self.url)

    async def close(self):
        logger.info(__name__)
        await self.instance.close()
        await self.playwright.stop()
