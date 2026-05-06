from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models.base import Base
from app.db.session import engine
    
from app.api.routers.task import router as task_router
    
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine) 
    yield
    
    

app = FastAPI(lifespan=lifespan)
app.include_router(router = task_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)


    
    




'''
            
class CategorySchema(BaseModel):
    id: str
    name: str
    
class CategoryCreateSchema(BaseModel):
    name: str
    
class CategoryUpdateSchema(BaseModel):
    name: str | None = None
    
categories:list[CategorySchema] = []


def category_orm_to_model (category: CategoryORM) -> CategorySchema:
    return CategorySchema(id=category.id,name=category.name)


@app.get("/categories")
def read_categories(db: Session = Depends(get_db)) -> list[CategorySchema]:
    categories = db.scalars(select(CategoryORM)).all()
    return [category_orm_to_model(cat) for cat in categories]


@app.post("/categories", status_code=status.HTTP_201_CREATED)
def create_category(payload:CategoryCreateSchema    , db: Session = Depends(get_db)) -> CategorySchema:
    new_category = CategoryORM(name=payload.name)
    
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return category_orm_to_model(new_category)


@app.patch("/categories/{category_id}")
def update_category (category_id: str, payload: CategoryUpdateSchema, db: Session = Depends(get_db)) -> CategorySchema:
    category = db.get(CategoryORM, category_id)
    
    if not category:
            raise HTTPException(status_code=404, detail="Category not found")
            return category


@app.delete("/categories/{category_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_category (category_id: str, db: Session = Depends(get_db)):
    for category in categories:
        if category.id == category_id:
            categories.remove(category)
            return
'''        
        
            
            
            


    
