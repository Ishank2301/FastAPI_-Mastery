from fastapi import FastAPI

app = FastAPI()


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"meassage": "This is an Practise tut for FastAPI "}


@app.get("/view")
def view():
    data = load_data()
    return data


@app.get("/view")
def view():
    data = load_data()
    return data
