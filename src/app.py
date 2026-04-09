from fastapi import FastAPI
from src.routes.user_router import router  # langsung dari file

app = FastAPI()
app.include_router(router)