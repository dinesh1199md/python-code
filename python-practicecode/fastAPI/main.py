from fastapi import FastAPI,status, Response,HTTPException,Path
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

# python -m uvicorn main:app --reload

class Blog(BaseModel):
    name: str
    description: str | None=None
    price: float
    publish: Optional[bool]


@app.get("/",status_code=status.HTTP_200_OK)
def index():
    return {"name":"dinesh","age":23,"place":"salem"}

@app.get("/about")
def about():
    return {"about":{"this is about page"}}

@app.get("/publish")
def publish(linmit : int = 100 ,publish: bool= True,sort:Optional[str]=None):
    
    if publish:
        return {"blogs":f"{linmit} published blogs available"} 
    else:
        return {"blogs":f"{linmit}  blogs available"}


@app.get("/blog/{id}")
def blog(id: int= Path(None,description="The Id should be not be Empty")):
    return {"count":id}

@app.get("/blog/{id}/comments")
def comments(id :int):    # type hint
    return {"comments":{id}}

'''create the post'''
@app.post("/blogs",status_code= status.HTTP_404_NOT_FOUND)
def blogpost(blog: Blog):
    return {"blog":f"this is the blog {blog.name} and description is {blog.description}"}

'''exception''' 
@app.get("/exception/{id}")
def statuscode(response: Response,id):
    l=[1,2,3,4,5,6,7,8,9]
    if id in l:
        return id
    else:
        #  response.status_code =(status.HTTP_404_NOT_FOUND )
        #  return {"the given id is not available in Db"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Requesting Id is Not Availble in Db")
    
if __name__=="__main__":
    # uvicorn.run(app,port=8001)
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
