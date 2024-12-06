from fastapi import FastAPI,Path,Query,Body,status,File,UploadFile,HTTPException,Depends
import uvicorn
from enum import Enum
from typing import Union,Annotated,Literal,List
from pydantic import BaseModel, Field

app=FastAPI()
class Item(BaseModel):
    name: str
    description: Union[str,None]= None
    price: float= Field(0,le=30)
    tax: float= None
    # tags: List[str] = []

class UserDetails(str, Enum):
    name="dinesh"
    age="18"
    place="Salem"

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=10
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None

@app.put("/items22/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

@app.get("/")
async def get():
    return{"Hello this is Dinesh"}

#query parameter
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# Query parameters with Option
@app.get("/items/{item_id}")
async def read_item(item_id: str, requireid: int, defultquery:str="HELLO", q: str = None): # q: Union[str,None] = None
    if q:
        return {"item_id": item_id, "q": q}
    
    return {"item_id": item_id,"requiredquery":requireid,"Defultquery":defultquery}

# Multiple path and query parameters 
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str = None, short: bool=True ):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/users/me")
async def read_user_me(current_user:str):
    return {"current_user": current_user}

#Path parameter
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

#Enumerate default value set
@app.get("/user/details/{userdetails}")
async def user_details(userdetails: UserDetails):
    if userdetails is UserDetails.name:
        return {"user_name": userdetails, "message": "valid users!"}
    if userdetails.value=="18":
         return {"user_age": userdetails, "message": "user is major!"}
    return {"user_Place": userdetails, "message": "I am valid user's location!"}

#Request body
@app.post("/items/reqbody",tags=["req_bosy"])
async def req_body(item:Item):
    tax_cal=item.dict()
    if item.tax:
        price_with_tax=item.price+ item.tax
        tax_cal.update({"price_with_tax":price_with_tax})
    return tax_cal

#Request body with pathparameter
@app.post("/items/reqbody/{item_id}",tags=["req_bosy"])
async def req_body_path(item:Item,itemid:int):
    user=item.dict()
    if itemid:
        user.update({"body_with_itemid":itemid})
    return user

#Request body with path and query parameter
@app.post("/items/reqbody_path_query/{item_id}",tags=["req_bosy"])
async def req_body_path_query(item:Item,itemid:int=None,q: str=None):
    user=item.dict()
    if itemid:
        user.update({"body_with_itemid":itemid})
    if q:
        user.update({"query_parameter":q})
    return user

# Query parameter with string validation
@app.get("/itemsquery/")
async def read_items(
    q: Annotated[Union[str,None], Query(min_length=0,max_length=10)]=None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Query parameter with string validation and pattern match
@app.get("/itemspatern/")
async def read_items2(
    q: Annotated[Union[str,None], Query(min_length=3, max_length=50, pattern="^fixedquery$")]=None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Path parameter with integer validation 
@app.get("/itemspath/{item_id}")
async def read_items3( item_id: Annotated[int,Path(title="check",ge=10,le=1000)] ,
                      size: Annotated[float, Query(gt=0, lt=10.5)],
    q: Annotated[Union[str,None], Query(min_length=3, max_length=50)]=None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#status code
@app.post("/stausvode/", status_code=status.HTTP_201_CREATED,tags=["status_code"])
async def create_item(name: str):
    return {"name": name}

#upload files 
@app.post("/files/",tags=["files"])
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/",tags=["files"])
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.post("/uploadfile2/",tags=["files"])
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}

#Multiplefiles upload
@app.post("/mul_files/",tags=["multi_files"])
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/multi_uploadfiles/",tags=["multi_files"])
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}

#Exception Hnadling 
items = {"foo": "The Foo Wrestlers","dinesh":"Great Man","mari": "Legend"}
@app.get("/exception/{item_str}")
async def read_item(item_str: str):
    if item_str not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_str]}



##Dependancy injection
async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/",tags=["Denpends"])
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/",tags=["Denpends"])
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons

##Class as a dependancy
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/depends_class/",tags=["Denpends"])
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response

## Depends with yield 
async def get_db():
    # db = DBSession()
    db = "dp session"
    try:
        yield db
    finally:
        db.close()

if __name__=="__main__":
    uvicorn.run("fast1:app", reload=True, port=5000)

