import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/quote/")
def quote():
    response = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=json")
    return response.json()["quoteText"]
