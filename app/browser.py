from playwright.sync_api import sync_playwright


def launch_browser():

    #Launch a Chromium browser instance.
    #Centralizes browser configuration so every extractor uses the same settings

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=True)

    return playwright, browser