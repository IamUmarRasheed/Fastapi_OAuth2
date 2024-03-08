from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get('/hi')
def greet():
    return 'hello world'


@app.get('/hi/{name}')
def greetname(name:str):
    return 'hello ? world ' + name


if __name__ == "__main__":
    import unicorn
    unicorn.run('hello:app',reload=True)