# Analyzer's job is to determine what is on a webpage for an automated system to interact with or extract

from app.browser import launch_browser     #Browser manager used
from app.analyzer.models import PageAnalysis
from app.analyzer.registry import ELEMENT_EXTRACTORS


def analyze_page(url):

    playwright, browser = launch_browser()

    page = browser.new_page()

    page.goto(url)

    analysis = PageAnalysis() 

    analysis.url = page.url
    analysis.title = page.title()
    
    #Automatically executes EVERY registered analyzer (even if new additions are made to registry)
    #Since 1st element in registry is buttons,
    #1st iteration of loop: name= "buttons", extractor= extract_buttons
    #Then it runs extractor(page) which is same as extract_buttons(page)
    for name, extractor in ELEMENT_EXTRACTORS.items():

        #setattr basically does analysis.name = extractor(page)
        #which i initially wrote as analysis.buttons= extract_buttons(page)
        setattr(
            analysis,
            name,
            extractor(page)
        )
    #Loop then iterates over next extractor element in registry

    browser.close()
    playwright.stop()

    return analysis