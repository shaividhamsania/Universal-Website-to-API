from playwright.sync_api import Page


def extract_buttons(page: Page):
    buttons = []

    button_elements = page.locator("button")

    for button in button_elements.all():

        #Storing dictionaries and not objects cause AI can read JSON data
        buttons.append(
            {
                "text": button.text_content(),
                "id": button.get_attribute("id"),
                "class": button.get_attribute("class"),
                "type": button.get_attribute("type")
            }
        )

    return buttons