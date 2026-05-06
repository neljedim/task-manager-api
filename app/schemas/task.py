from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: str
    title: str
    completed: bool
    category_id: str | None = None
    
    
class TaskCreateSchema(BaseModel):
    title: str
    category_id: str | None = None  
    
class TaskUpdateSchema(BaseModel):
    title:str | None = None
    completed: bool | None = None 