import os
import pytest
from app.core.playwrightbrowser import PlaywrightBrowser
from app.core.filedefinitions import FileDefinitions


@pytest.fixture
def browser():
    FileDefinitions()
    return PlaywrightBrowser(browser_type=os.getenv("BROWSER").lower())


@pytest.fixture
async def page(browser):
    await browser.setup()
    await browser.open_url(url=os.getenv("URL"))
    return browser.page
