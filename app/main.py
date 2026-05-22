from fastapi import FastAPI
from app.finance.router import router as router_finance
from app.users.router import router as router_users

app = FastAPI()


app.include_router(router_finance)
app.include_router(router_users)