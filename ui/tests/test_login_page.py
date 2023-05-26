from dotenv import dotenv_values
from playwright.sync_api import expect


def test_login_page_login_unknown_email(home_page, login_page):
    """
    Test case to verify login with an unknown email.
    It checks for the display of error messages when logging in with an unknown email.

    Steps:
    1. Retrieve the unknown email from the environment variables.
    2. Navigate to the home page.
    3. Click on the login button in the header.
    4. Fill in the unknown email in the login page.
    5. Click on the continue button.
    6. Expect the email is invalid modal to be visible.
    7. Click on the try again button.
    8. Expect the email error message to be visible.
    9. Expect the email error message to have the correct text.
    """

    error_message = "Unknown email. Please check your spelling."
    email = dotenv_values()["USERNAME"]

    home_page.go_to()
    home_page.header_login_button.click()

    login_page.fill_email(email)
    login_page.continue_button.click()
    expect(login_page.email_is_invalid_modal).to_be_visible()
    login_page.try_again_button.click()
    expect(login_page.email_error_message).to_be_visible()
    expect(login_page.email_error_message).to_have_text(error_message)


def test_login_page_login_not_valid_email(home_page, login_page):
    """
    Test case to verify login with an invalid email format.
    It checks for the display of error messages when logging in with an invalid email format.

    Steps:
    1. Define an invalid email format.
    2. Navigate to the home page.
    3. Click on the login button in the header.
    4. Fill in the invalid email in the login page.
    5. Click on the continue button.
    6. Expect the email error message to be visible.
    7. Expect the email error message to have the correct text.
    """

    error_message = "Sorry, we are having trouble creating your account. Please re-enter your email and password and try again. If the problem persists, contact Disney+ Support (Error Code 6)."
    email = "NOTVALIDEMAIL"

    home_page.go_to()
    home_page.header_login_button.click()

    login_page.fill_email(email)
    login_page.continue_button.click()
    expect(login_page.email_error_message).to_be_visible()
    expect(login_page.email_error_message).to_have_text(error_message)


def test_login_page_sign_up_unknown_email(home_page, login_page):
    """
    Test case to verify sign-up with an unknown email.
    It checks the flow of signing up with an unknown email.

    Steps:
    1. Retrieve the unknown email from the environment variables.
    2. Navigate to the home page.
    3. Click on the login button in the header.
    4. Fill in the unknown email in the login page.
    5. Click on the continue button.
    6. Expect the email is invalid modal to be visible.
    7. Click on the sign-up button.
    """

    email = dotenv_values()["USERNAME"]

    home_page.go_to()
    home_page.header_login_button.click()

    login_page.fill_email(email)
    login_page.continue_button.click()
    expect(login_page.email_is_invalid_modal).to_be_visible()
    login_page.sign_up_button.click()
