from playwright.sync_api import sync_playwright
import time


def select_somalia_and_set_amount(page, amount=100):
    """
    Ensures Somalia is selected and sets the amount in the money box

    Args:
        page: Playwright page object
        amount: Amount to set (default: 100)
    """
    try:
        cookie_button = page.locator("#CybotCookiebotDialogBodyButtonAccept")
        if cookie_button.is_visible(timeout=5000):
            print("Cookie dialog detected. Accepting cookies.")
            cookie_button.click()
            page.wait_for_timeout(1000)
        # Wait for the money boxes to be visible
        page.wait_for_selector(".money-box.source-box", timeout=5000)

        # Get the second money box
        somalia_box = page.locator(".money-box.source-box").nth(1)

        # Check if Somalia is selected by looking for the SO flag
        somalia_flag = somalia_box.locator("img[alt='icon flag SO']")

        if not somalia_flag.is_visible():
            print("Somalia not selected, selecting it now...")

            # Click the currency selector button in the second box
            selector_button = somalia_box.locator("button.selector")
            selector_button.click()

            # Wait for any dropdown or currency options to appear
            page.wait_for_timeout(1000)  # Adjust timeout as needed

            try:
                # Try different methods to select Somalia
                # Method 1: Direct Somalia option click if visible
                somalia_option = page.locator("img[alt='icon flag SO']").first
                if somalia_option.is_visible():
                    somalia_option.click()
                else:
                    # Method 2: Try finding Somalia in a dropdown list
                    somalia_item = page.locator("li:has-text('Somalia')").first
                    if somalia_item.is_visible():
                        somalia_item.click()
                    else:
                        # Method 3: Try finding by currency code
                        usd_option = page.locator("span.currency-code:has-text('USD')").first
                        if usd_option.is_visible():
                            usd_option.click()
                        else:
                            raise Exception("Could not find Somalia/USD option")

                # Wait for selection to take effect
                page.wait_for_timeout(1000)

                # Verify Somalia was selected
                if not somalia_flag.is_visible():
                    raise Exception("Failed to select Somalia")

            except Exception as e:
                print(f"Error selecting Somalia: {e}")
                return False

        # Now set the amount
        amount_input = somalia_box.locator("input[aria-label='Money input Somalia']")
        amount_input.click()
        amount_input.fill(str(amount))

        print(f"Successfully set amount to {amount} in Somalia money box")

        # Verify the amount was set
        amount_holder = somalia_box.locator(".amount-holder")
        try:
            page.wait_for_timeout(1000)  # Give time for calculations
            displayed_amount = amount_holder.text_content()
            print(f"Displayed amount: {displayed_amount}")
        except Exception as e:
            print(f"Note: Couldn't verify final amount: {e}")

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for production
        page = browser.new_page()

        # Navigate to the website (replace with actual URL)
        page.goto("https://www.dahabshiil.com/")

        # Wait for page to load
        page.wait_for_load_state("networkidle")

        # Select Somalia if needed and set amount
        success = select_somalia_and_set_amount(page)

        if not success:
            print("Failed to complete the operation")

        # Optional: Wait to see the result
        time.sleep(2)

        browser.close()


if __name__ == "__main__":
    main()