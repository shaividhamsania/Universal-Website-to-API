#Registry so that every time website HTML introduces new element, we don't have to edit analyzer.py 

from app.analyzer.elements import extract_buttons

ELEMENT_EXTRACTORS = {
    "buttons": extract_buttons,
}