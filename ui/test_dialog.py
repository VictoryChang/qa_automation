from icecream import ic
from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope='module')
def browser(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

messages = []

def handle_dialog(dialog):
    messages.append(dialog.message)
    dialog.accept()

dismiss_messages = []

def dismiss_dialog(dialog):
    dismiss_messages.append(dialog.message)
    dialog.dismiss()


def enter_dialog(dialog):
    dialog.accept('Your Name')


def test_dialog_accept(page):
    page.goto('https://demo.automationtesting.in/Alerts.html')
    page.locator('//a[@href="#CancelTab"]').click()
    page.on('dialog', handle_dialog)
    page.locator('//div[@id="CancelTab"]/button').click()
    ic(messages)
    assert messages[0] == 'Press a Button !'
    assert page.locator('//p[@id="demo"]').text_content() == 'You pressed Ok'


def test_dialog_dismiss(page):
    page.goto('https://demo.automationtesting.in/Alerts.html')
    page.locator('//a[@href="#CancelTab"]').click()
    page.on('dialog', dismiss_dialog)
    page.locator('//div[@id="CancelTab"]/button').click()
    ic(dismiss_messages)
    assert dismiss_messages[0] == 'Press a Button !'
    assert page.locator('//p[@id="demo"]').text_content() == 'You Pressed Cancel'


def test_dialog_textbox(page):
    page.goto('https://demo.automationtesting.in/Alerts.html')
    page.locator('//a[@href="#Textbox"]').click()
    page.on('dialog', enter_dialog)
    page.locator('//div[@id="Textbox"]/button').click()
    assert page.locator('//p[@id="demo1"]').text_content() == 'Hello Your Name How are you today'


