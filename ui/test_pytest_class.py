from icecream import ic
from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope='class')
def browser(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        request.cls.browser = browser
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.mark.usefixtures('browser')
class TestTitle:
    def test_goto_google(self, page):
        page.goto('https://www.google.com')
        assert page.title() == 'Google'

    def test_goto_orange(self, page):
        page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        assert page.title() == 'OrangeHRM'