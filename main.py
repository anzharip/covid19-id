from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    # Load the data from file
    with open('covid_data.json') as json_file:
        covid_data = json.load(json_file)
    return covid_data