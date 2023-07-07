from playwright.sync_api import Page
from dotenv import dotenv_values
from playwright.sync_api import expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.header_login_button = page.locator(
            "[data-testid='log_in_header'] >> nth=0"
        )
        self.new_on_disney_plus_tab = page.locator("#tab-NEWONDISNEY")
        self.trending_tab = page.locator("#tab-TRENDING")
        self.coming_soon = page.locator("#tab-COMINGSOON")
        self.us_plan_section = page.locator(
            "//section[@id='us-plan-comp']"
        )
        self.us_plan_title = page.locator(
            "//span[@class='h2']"
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
        assert self.header_login_button.is_visible()
        assert self.new_on_disney_plus_tab.is_visible()
        assert self.trending_tab.is_visible()
        assert self.coming_soon.is_visible()

    def test_banner_visibility(self):
        """
        Test the visibility of the banner.
        """
        assert self.us_plan_section.is_visible()

    def test_us_plan_section_text_content(self, text):
        """
        Test the text content of the banner.
        """
        expect(self.us_plan_section).to_be_visible()
        expect(self.us_plan_title).to_have_text(text)
