from fastapi import FastAPI,Path, Query
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    Name:str
    Price:float
    Brand:Optional[str]=None
    
class ItemUpdate(BaseModel):
    Name:str = None
    Price:float = None
    Brand:Optional[str]=None

inventory={
    1:{
        "Name":"Milk",
        "Price":399,
        "Brand":"Amul"
    }

}
@app.get("/get-item/{item_id}")
def get_item(item_id:int=Path(description="The ID of the item you want to view"),gt=0):
     return inventory[item_id]

@app.get("/get-by-name")
def get_item(*,name:Optional[str]=None,price:int):
     for i in inventory:
          if inventory[i]['Name']==name or inventory[i]['Price']==price:
               return inventory[i]

     return {"Data":"Not found"}

@app.post("/create-item/{item_id}")
def create_item(item:Item,item_id:int):
     if item_id in inventory:
          return {"Error":"Item ID already exists"}

     inventory[item_id]=item
     return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item:ItemUpdate,item_id:int):
     if item_id not in inventory:
          return {"Error":"Item ID does not exist"}

     if item.Name != None:
          inventory[item_id].Name=item.Name
     if item.Price != None:
          inventory[item_id].Price=item.Price
     if item.Brand != None:
          inventory[item_id].Brand=item.Brand

     return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id:int = Query(...,description="The ID of the item you want to delete",gt=0)):
     if item_id not in inventory:
          return {"Error":"Item ID does not exist"}

     del inventory[item_id]
     return {"Success":"Item deleted successfully"}
#GET
#POST
#PUT
#DELETE