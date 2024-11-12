from playwright.sync_api import sync_playwright

def fetch_transfer_quotes():
    with sync_playwright() as p:
        # Open a new browser instance
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the URL
        url = "https://transfergalaxy.com/en/destination/somalia/"
        page.goto(url)

        try:
            url = "https://transfergalaxy.com/en/destination/somalia/"
            page.goto(url)

            # Handle cookie dialog
            cookie_button = page.locator("#CybotCookiebotDialogBodyButtonAccept")
            if cookie_button.is_visible(timeout=5000):
                print("Cookie dialog detected. Accepting cookies.")
                cookie_button.click()
                page.wait_for_timeout(1000)

            # Try multiple different selectors for the sending country dropdown
            # Method 1: Using the select element directly
            try:
                dropdown = page.locator("#SendingCountryAlpha3")
                dropdown.select_option("GBR")  # Using the value from your HTML
                print("Selected using direct select")
            except Exception as e:
                print(f"Direct select failed: {e}")

                # Method 2: Click the button first
                try:
                    button = page.locator("button[aria-owns='bs-select-1']")
                    button.click()
                    page.wait_for_timeout(1000)

                    # Try clicking the UK option
                    uk_option = page.locator("option[value='GBR']")
                    uk_option.click()
                    print("Selected using button click")
                except Exception as e:
                    print(f"Button click failed: {e}")

                    # Method 3: Try using the Bootstrap select container
                    try:
                        container = page.locator("div.bootstrap-select.preferred-country-select").first
                        container.click()
                        page.wait_for_timeout(1000)

                        uk_item = page.locator("span.flag.GBR").first
                        uk_item.click()
                        print("Selected using container click")
                    except Exception as e:
                        print(f"Container click failed: {e}")

            page.wait_for_timeout(2000)

            page.wait_for_selector("div.calculation", timeout=10000)

            sending_amount = page.locator(
                "div.calculation table.index-table tbody tr:has(th:text('You send')) td").text_content()
            fees_text = page.locator(
                "div.calculation table.index-table tbody tr:has(th:text('Our fee')) td").text_content()
            exchange_rate_text = page.locator(
                "div.calculation table.index-table tbody tr:has(th:text('Exchange rate')) td").text_content()

            print(f"You send: {sending_amount}")
            print(f"Fee: {fees_text}")
            if exchange_rate_text:
                exchange_rate = exchange_rate_text.split("=")[-1].strip().split(' ')[0]
                print(f"Exchange Rate: {exchange_rate}")
            else:
                print("Exchange rate not found")

        except TimeoutError:
            print("Timed out waiting for calculation results")

        except Exception as e:
            print(f"An error occurred: {e}")
            import traceback
            traceback.print_exc()
        finally:
            browser.close()

if __name__ == "__main__":
    fetch_transfer_quotes()