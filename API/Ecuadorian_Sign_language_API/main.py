from fastapi import FastAPI
from routes.user_routes import lexer_router, router
from crud.user_crud import user_crud, palabra_crud, caracter_crud
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
#adding cors uris
origins =[    
    #"http://localhost:8000",  
    "http://0.0.0.0:0000",
    "https://0.0.0.0:0000",
    "http://localhost:4200",    
]

#adding middleware uris
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(lexer_router, prefix="/logic")
app.include_router(user_crud, prefix="/crud")
app.include_router(caracter_crud, prefix="/crud")
app.include_router(palabra_crud, prefix="/crud")
app.include_router(router, prefix="/logic")

app.mount("/videos", StaticFiles(directory="videos"), name="videos")

