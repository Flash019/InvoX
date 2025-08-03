from fastapi import FastAPI
from backend.router import user, authentication

app = FastAPI(title="InvoX")

app.include_router(authentication.router)
app.include_router(user.router)
