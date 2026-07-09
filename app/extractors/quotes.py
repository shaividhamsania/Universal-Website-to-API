from playwright.sync_api import sync_playwright


def extract_quotes():

    quotes = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            "https://quotes.toscrape.com/",
            wait_until="networkidle"
        )

        quote_cards = page.locator(".quote")

        total_quotes = quote_cards.count()

        for i in range(total_quotes):
            card = quote_cards.nth(i)

            quote_text = card.locator(".text").text_content()
            author = card.locator(".author").text_content()

            quotes.append(
                {
                    "quote": quote_text,
                    "author": author
                }
            )

        browser.close()

    return quotes