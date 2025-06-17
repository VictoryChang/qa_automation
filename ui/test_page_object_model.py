from icecream import ic
from playwright.sync_api import Page, sync_playwright
import pytest


@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


class OrangeHrmHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator('//input[@name="username"]')
        self.password = page.locator('//input[@name="password"]')
        self.submit = page.locator('//button[@type="submit"]')

    def navigate(self):
        self.page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def login(self, username: str, password: str):
        self.username.type(username)
        self.password.type(password)
        self.submit.click()


def test_login_orange(page):
    homepage = OrangeHrmHomePage(page)
    homepage.navigate()
    homepage.login(username='Admin', password='admin123')
    page.wait_for_timeout(3000)
    assert page.url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
