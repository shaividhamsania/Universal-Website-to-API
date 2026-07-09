from playwright.sync_api import sync_playwright


def search_wikipedia(topic: str, paragraphs: int = 3):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            f"https://en.wikipedia.org/wiki/{topic}",
            wait_until="networkidle"
        )

        text = [
            paragraph.strip()
            for paragraph in page.locator("p").all_text_contents()
            if paragraph.strip()
        ]
        browser.close()

    return {
        "topic": topic,
        "paragraphs": text[:paragraphs]
    }