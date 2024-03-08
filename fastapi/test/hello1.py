from fastapi import FastAPI

app : FastAPI = FastAPI()
@app.get('/')
def myfun():
    return 'hello fatapi'