from app.browser import launch_browser

#Extract all books on homepage
#Returns list of dictionaries containing title, price, rating
def extract_books():

    books = []

    playwright, browser= launch_browser()

    page = browser.new_page()

    page.goto(
        "https://books.toscrape.com/",
        wait_until="networkidle"
    )

    book_cards = page.locator(".product_pod")

    total_books = book_cards.count()

    #Iterates through each book card found and converts to structured JSON
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
    playwright.stop()

    #Returns extracted data so it can be reused by FastAPI endpoints
    return books