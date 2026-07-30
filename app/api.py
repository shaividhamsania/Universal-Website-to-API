from fastapi import FastAPI

from app.analyzer.analyzer import analyze_page
from app.ai.planner import generate_workflow

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


#temporary ai path test endpoint
@app.get("/plan")    #tells FastAPI when sent a GET request to /plan (by using swagger), execute the function below
def plan(
    #a step to satisfy the 'universal' bit of the project
    url: str,     #creates the 1st API parameter (a 'url' textbox in swagger for entering website url)
    goal: str,     #creates another API parameter (a 'goal' textbox in swagger for the goal for example: "extract every quote and author")
):

    #where analyzer runs to analyze every element of the website
    #analysis object stores the returned PageAnalysis object with all buttons, forms, etc.
    analysis = analyze_page(url)      

    workflow = generate_workflow(
        analysis,      #sends entire analyzed object to llm
        goal,      #sends the user's goal to the llm
    )
    #the above function returns a json format of workflow steps and gets stored in workflow

    return {
        "workflow": workflow      #workflow is returned
    }