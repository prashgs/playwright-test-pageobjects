from time import sleep
import pytest


@pytest.mark.asyncio
async def test_homepage(browser, page):
    google_page = await page
    sleep(10)
