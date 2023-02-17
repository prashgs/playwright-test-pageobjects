import os
import re

import pytest
from playwright.sync_api import expect, Page

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
def test_homepage(page: Page, data):
    logger.info(__name__)
    page.goto(os.environ['URL'])
    computers_page = ComputersPage(page=page)

    add_computer_page = AddComputerPage(page=page)
    for item in data.newComputers:
        computers_page.add_new_computer()
        add_computer_page.add(item)
        add_computer_page.create_computer()
        expect(page.locator(computers_page.selectors.alert_message)).to_have_text(re.compile(item.computerName))
