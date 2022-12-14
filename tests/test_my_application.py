import os
import re

import pytest
from playwright.async_api import expect

from src.core.filedefinitions import FileDefinitions
from src.core.logger import logger
from src.helpers.utils import read_data_file
from src.models.newcomputermodel import NewComputersModel
from src.pages.addcomputerpage import AddComputerPage
from src.pages.computerspage import ComputersPage


@pytest.fixture
def data() -> dict:
    DATA_FILE = os.path.join(FileDefinitions.data_dir, 'newComputers.json')
    data = read_data_file(DATA_FILE, type='json')
    data = NewComputersModel(**data)
    return data


@pytest.mark.asyncio
async def test_homepage(browser, page, data):
    logger.info(__name__)
    homepage = await page
    computers_page = ComputersPage(page=homepage)

    add_computer_page = AddComputerPage(page=homepage)
    for item in data.newComputers:
        await computers_page.add_new_computer()
        await add_computer_page.add(item)
        await add_computer_page.create_computer()
        await expect(homepage.locator(computers_page.selectors.alert_message)).to_have_text(re.compile(item.computerName))


        