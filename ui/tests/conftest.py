import pytest
from playwright.sync_api import sync_playwright
from ui.pages.home_page import HomePage
from ui.pages.login_page import LoginPage


@pytest.fixture(scope="session")
def browser():
    """
    Fixture to initialize the browser session and launch the browser.
    """
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """
    Fixture to create a new page within the browser context.
    """
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def home_page(page):
    """
    Fixture to create an instance of the home page.
    """
    home_page = HomePage(page)
    home_page.go_to()
    return home_page


@pytest.fixture
def login_page(page):
    """
    Fixture to create an instance of the login page.
    """
    login_page = LoginPage(page)
    return login_page
