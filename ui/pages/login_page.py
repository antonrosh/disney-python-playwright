from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#email")
        self.continue_button = page.get_by_test_id("login-continue-button")
        self.email_is_invalid_modal = page.locator('[role="dialog"]')
        self.sign_up_button = page.get_by_test_id("modal-secondary-button")
        self.try_again_button = page.get_by_test_id("modal-primary-button")
        self.email_error_message = page.locator("#email__error")
        self.agree_and_continue_button = page.get_by_test_id("signup-continue-button")

    def fill_email(self, email):
        """
        Fill the email input field with the provided email.
        """
        self.email_input.fill(email)
