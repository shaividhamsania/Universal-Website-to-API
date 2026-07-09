from playwright.sync_api import sync_playwright


def extract_books():

    books = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            "https://books.toscrape.com/",
            wait_until="networkidle"
        )

        book_cards = page.locator(".product_pod")

        total_books = book_cards.count()

        for i in range(total_books):

            book = book_cards.nth(i)

            title = book.locator("h3 a").get_attribute("title")

            price = book.locator(".price_color").text_content()

            rating = book.locator(".star-rating").get_attribute("class")

            books.append(
                {
                    "title": title,
                    "price": price,
                    "rating": rating.replace("star-rating ", "")
                }
            )

        browser.close()

    return books