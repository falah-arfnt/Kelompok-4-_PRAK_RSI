from fastapi import FastAPI

from src.routes.user_router import router as user_router
from src.routes.role_router import router as role_router
from src.routes.account_router import router as account_router
from src.routes.event_router import router as event_router
from src.routes.registration_router import router as registration_router

app = FastAPI()

app.include_router(user_router)
app.include_router(role_router)
app.include_router(account_router)
app.include_router(event_router)
app.include_router(registration_router)