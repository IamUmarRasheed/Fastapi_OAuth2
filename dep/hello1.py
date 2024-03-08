from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated
blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

def get_blog_or_error(id:str):
    name: blogs.get(id)
    if not name:
        raise HTTPException(status_code=status.HTTP_404_not_found,detail=f"Blog ID {id} not founf")
    return name


app:FastAPI=FastAPI(title='something')

@app.get('/blof/{id}')
def gee_blog(blogname:Annotated[str,Depends(get_blog_or_error)])
    return blogname