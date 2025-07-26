from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import form_post, form_get
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="KPA Form API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(form_post.router)
app.include_router(form_get.router)