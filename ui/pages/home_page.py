from playwright.sync_api import Page
from dotenv import dotenv_values
from playwright.sync_api import expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("[data-testid='input-email-email']")
        self.continue_button = page.locator("[data-testid='undefined_hero']")
        self.header_login_button = page.locator(
            "[data-testid='log_in_header'] >> nth=0"
        )
        self.new_on_disney_plus_tab = page.locator("#tab-NEWONDISNEY")
        self.trending_tab = page.locator("#tab-TRENDING")
        self.coming_soon = page.locator("#tab-COMINGSOON")
        self.banner = page.locator(
            "//div[@class='banner-content']//p//span[@class='fine'][1]"
        )

    def go_to(self):
        """
        Navigate to the home page URL.
        """
        self.page.goto(dotenv_values()["BASE_URL"])

    def verify_page_elements(self):
        """
        Verify the visibility of page elements.
        """
        assert self.email_input.is_visible()
        assert self.continue_button.is_visible()
        assert self.header_login_button.is_visible()
        assert self.new_on_disney_plus_tab.is_visible()
        assert self.trending_tab.is_visible()
        assert self.coming_soon.is_visible()

    def test_banner_visibility(self):
        """
        Test the visibility of the banner.
        """
        assert self.banner.is_visible()

    def test_banner_text_content(self, text):
        """
        Test the text content of the banner.
        """
        expect(self.banner).to_have_text(text)
