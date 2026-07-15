from fastapi import FastAPI

#Import extraction functions that contain Playwright automation logic for each supported website
from app.extractors.wikipedia import search_wikipedia
from app.extractors.books import extract_books
from app.extractors.quotes import extract_quotes

#FastAPI is the app's entry point
#Every endpoint defined below exposes one of the extractors as a reusable REST API.
app = FastAPI()


@app.get("/")
def home(): #Used to check whether API server runs correctly
    return {
        "message": "Universal Website-to-API Platform"
    }


@app.get("/wikipedia")
def wikipedia(topic: str, paragraphs: int = 3):

    #Retrieve paragraphs from wikipedia
    #FastAPI automatically converts the URL query-parameters into function args
    return search_wikipedia(topic, paragraphs)

@app.get("/books")
def books(
    max_price: float,
    min_rating: int
):

    filters= {
        "max_price": max_price,
        "min_rating": min_rating
    }

    #Retrieve book info
    #Returns a JSON array containing the books extracted with the filters mentioned
    return extract_books(filters)

@app.get("/quotes")
def quotes():

    #Retrieve quotes
    #Returns a JSON array containing the quotes extracted
    return extract_quotes()