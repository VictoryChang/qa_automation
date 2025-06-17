from icecream import ic
from playwright.sync_api import sync_playwright
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


def test_login_orange(page):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.locator('//input[@name="username"]').type('Admin')
    page.locator('//input[@name="password"]').type('admin123')
    page.locator('//button[@type="submit"]').click()
    assert page.url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'


@pytest.mark.parametrize('invalid_username, invalid_password', [('admin', 'admin'), ('abc', '123')])
def test_login_invalid_orange(page, invalid_username, invalid_password):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.locator('//input[@name="username"]').type(invalid_username)
    page.locator('//input[@name="password"]').type(invalid_password)
    page.locator('//button[@type="submit"]').click()
    alert_text = page.locator('//div[@role="alert"]//p').text_content()
    assert alert_text == 'Invalid credentials'