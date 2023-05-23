from playwright.sync_api import expect


def test_home_page_elements(home_page):
    """
    Test case to verify the presence of various elements on the home page.
    It checks for the visibility of email input, continue button, header login button,
    new on Disney Plus tab, trending tab, and coming soon tab.

    Steps:
    1. Create an instance of HomePage.
    2. Navigate to the home page.
    3. Verify the visibility of email input, continue button, header login button,
       new on Disney Plus tab, trending tab, and coming soon tab.
    """

    home_page.go_to()
    home_page.verify_page_elements()


def test_home_page_title(page, home_page):
    """
    Test case to verify the title of the home page.
    It checks if the title of the page matches the expected title.

    Steps:
    1. Define the expected title of the home page.
    2. Create an instance of HomePage.
    3. Navigate to the home page.
    4. Expect the page to have the specified title.
    """

    title = "Stream Disney, Pixar, Marvel, Star Wars, Nat Geo | Disney+"

    home_page.go_to()
    expect(page).to_have_title(title)


def test_home_page_banner(home_page):
    """
    Test case to verify the text content of the banner on the home page.
    It checks if the text content of the banner matches the expected text.

    Steps:
    1. Define the expected text content of the banner.
    2. Create an instance of HomePage.
    3. Navigate to the home page.
    4. Verify the text content of the banner.
    """

    text = "Available via Hulu.com only. Ends 5/27. Eligibility req’s &"

    home_page.go_to()
    home_page.test_banner_text_content(text)
