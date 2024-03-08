from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated, Any

blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

class Getobj():
  def  __init__(self,model)->None:
      self.model=model
      
      
    
   def __call__(self, id:str) -> None:
        obj=self.model.get(id)
        if not obj :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj
    
    
    app= FastAPI(title='something')
    

mydep= Getobj(blogs)


@app.get('/blog/{id}')
def  grt_bloh(blog_name:Annotated[str,depends(mydep)])
    return blog_name