from pydantic import BaseModel 
class Creature(BaseModel):
    name:str
    country:str
    area:str
    des:str
    aka:str

thing=Creature( name="yeti",
    country="CN",
    area="Himalayas",
    des="Hirsute Himalayan",
    aka="Abominable Snowman")


print('naem is ', thing.name)