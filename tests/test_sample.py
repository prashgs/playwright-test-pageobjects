from playwright.sync_api import Page, expect

URL = 'https://computer-database.gatling.io/computers'

def test_sample(page: Page):
    page.goto(url=URL, wait_until='load')
    expect(page).to_have_url(URL)

def test_navigates_page(page: Page) -> None:
    response = page.request.get(url=URL)
    expect(response).to_be_ok()