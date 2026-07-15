
from app.browser import launch_browser


def search_wikipedia(topic: str, paragraphs: int = 3):

    #Extract first N paragraphs from a wikipedia article
    #ARGS:
    #topic: article name, paragraphs:number of paragraphs to return
    #Returns dictionary containing article topic and extracted paragraphs.

    #Asks browser manager for a browser
    playwright, browser= launch_browser()

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
    playwright.stop()

    #Return strcutured data instead of printing it
    #allows FastAPI to reuse function
    return {
        "topic": topic,
        "paragraphs": text[:paragraphs]
    }