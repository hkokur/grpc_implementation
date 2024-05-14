from fastapi import FastAPI
from routers.orders import router as order_router

app = FastAPI()

app.include_router(order_router)

@app.get("/")
async def root():
    return {"message": "success"}
