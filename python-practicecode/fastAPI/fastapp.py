from fastapi import FastAPI
from pydantic import BaseModel,validator,conint
import json,uvicorn

app=FastAPI()



class Item(BaseModel):
    name: str
    id: int
class Check(BaseModel):
    name: str
    age: int
    @validator('age')
    def check_age(cls,value):
        if value<=30:
            raise ValueError("age must be greater than 30")
        return value
    
class Check2(BaseModel):
    name: str 
    # age: conint(gt=30)






@app.get("/poly")
def findpolindrome():
    print("Inside polindrome check")
    return f"Inside polindrome check"

@app.get("/poly/{poliystring}")
def findpolindrome1(poliystring:str):
    return {"polindrome",poliystring==poliystring[::-1]}

@app.get("/helo/{multistring}")
def findpolindrome2(multistring:str):
    dic={}
    for string in multistring.split("-"):
        dic[string]=(string==string[::-1])
    print(dic)    
    return json.dumps(dic) 

@app.post("/validate_age/")
def validateage(check:Check):
    return {"message": f"welcome{check.name}, you are {check.age} years old"}
@app.post("/validate_agecheck2/")
def validateage(check:Check2):
    return {"message": f"welcome{check.name}, you are {check.age} years old"}

if __name__=="__main__":
    uvicorn.run("fastapp:app",port=8001,reload=True)

# if __name__ == "__main__":
#     uvicorn.run("example:app", host="127.0.0.1", port=5000, reload=True)


# from fastapi import FastAPI
# import uvicorn

# app=FastAPI()

# @app.get("/")
# async def test():
#     return f"test msg"

# if __name__=="__main__":
#     uvicorn.run("fastapp:app",reload=True)
