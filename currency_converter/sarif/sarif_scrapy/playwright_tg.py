from playwright.sync_api import expect

def select_sending_country(page, country_code="GBR"):
    """
    Select a sending country on TransferGalaxy using multiple fallback methods.

    Args:
        page: Playwright page object
        country_code: Alpha-3 country code (default: "GBR" for United Kingdom)
    """
    url = "https://transfergalaxy.com/en/destination/somalia/"
    page.goto(url)

    # Wait for page to load completely
    page.wait_for_load_state("networkidle")

    # Handle cookie dialog
    cookie_button = page.locator("#CybotCookiebotDialogBodyButtonAccept")
    if cookie_button.is_visible(timeout=5000):
        cookie_button.click()
        page.wait_for_load_state("networkidle")

    # Method 1: Try using JavaScript to set the value directly
    try:
        page.evaluate(f"""
            document.querySelector('#SendingCountryAlpha3').value = '{country_code}';
            document.querySelector('#SendingCountryAlpha3').dispatchEvent(new Event('change'));
        """)
        print("Selected country using JavaScript")
        return True
    except Exception as e:
        print(f"JavaScript method failed: {e}")

    # Method 2: Try interacting with the Bootstrap Select UI
    try:
        # Click the bootstrap-select button to open the dropdown
        page.locator("button.dropdown-toggle[data-id='SendingCountryAlpha3']").click()

        # Wait for dropdown to be visible
        page.wait_for_selector(".dropdown-menu.show", timeout=5000)

        # Click the specific country option
        page.locator(f".dropdown-menu li[data-original-index] a[data-tokens*='{country_code}']").click()

        print("Selected country using Bootstrap Select UI")
        return True
    except Exception as e:
        print(f"Bootstrap Select UI method failed: {e}")

    # Method 3: Force visibility and use native select
    try:
        # Make the select element visible using JavaScript
        page.evaluate("""
            const select = document.querySelector('#SendingCountryAlpha3');
            select.style.opacity = '1';
            select.style.position = 'static';
            select.style.visibility = 'visible';
        """)

        # Now try to use the native select
        select = page.locator("#SendingCountryAlpha3")
        select.select_option(country_code)

        print("Selected country using forced visibility")
        return True
    except Exception as e:
        print(f"Forced visibility method failed: {e}")

    return False


# Usage example
def main():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True in production
        page = browser.new_page()

        success = select_sending_country(page)
        if success:
            # Wait a moment to verify the change
            page.wait_for_timeout(2000)

            # Optional: Verify the selection worked
            selected_value = page.evaluate("document.querySelector('#SendingCountryAlpha3').value")
            print(f"Selected value: {selected_value}")

        browser.close()


if __name__ == "__main__":
    main()