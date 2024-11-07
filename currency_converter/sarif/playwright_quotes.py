from playwright.sync_api import sync_playwright

def fetch_transfer_quotes():
    with sync_playwright() as p:
        # Open a new browser instance
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the URL
        url = "https://transfergalaxy.com/en/destination/somalia/"
        page.goto(url)

        # Make the Sending location United Kingdom
        page.locator("div.row ").click()
        page.locator("").click()
        # Extract rate
        sending_amount = page.locator("div.calculation table.index-table tbody tr:has(th:text('You send')) td").text_content()
        print(f"You send: {sending_amount}")
        fees_text = page.locator("div.calculation table.index-table tbody tr:has(th:text('Our fee')) td").text_content()
        print(f"Fee: {fees_text}")
        exchange_rate_text = page.locator("div.calculation table.index-table tbody tr:has(th:text('Exchange rate')) td").text_content()

        if exchange_rate_text:
            exchange_rate = exchange_rate_text.split("=")[-1].strip().split(' ')[0]
            print("Exchange Rate:", exchange_rate)
        else:
            print("Exchange rate not found")

        browser.close()

fetch_transfer_quotes()