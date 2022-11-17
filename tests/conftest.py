import os
import pytest
from src.core.playwrightbrowser import PlaywrightBrowser
from src.core.logger import logger


@pytest.fixture
def browser():
    logger.info(__name__)
    return PlaywrightBrowser(browser_type=os.getenv("BROWSER").lower())


@pytest.fixture
async def page(browser):
    logger.info(__name__)
    await browser.setup()
    await browser.open_url(url=os.getenv("URL"))
    return browser.page
