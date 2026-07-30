from dataclasses import dataclass, field

@dataclass
class PageElement:         #This class describes one HTML element like buttons
    tag: str= ""
    text: str= ""
    selector: str= ""
    id: str= ""
    class_name: str= ""
    attributed: dict= field(default_factory=dict)


@dataclass
class PageAnalysis:       #This class describes an entire webpage
    url: str = ""      #Stores website url
    title: str = ""

    #forms= [] reuses same list for every object
    #default_factory=list creates a new empty list every time you create a new PageAnalysis
    forms: list = field(default_factory=list)

    text_inputs: list = field(default_factory=list)
    textareas: list = field(default_factory=list)
    dropdowns: list = field(default_factory=list)
    checkboxes: list = field(default_factory=list)
    radio_buttons: list = field(default_factory=list)

    buttons: list = field(default_factory=list)

    links: list = field(default_factory=list)

    tables: list = field(default_factory=list)

    headings: list = field(default_factory=list)
    paragraphs: list = field(default_factory=list)

    images: list = field(default_factory=list)