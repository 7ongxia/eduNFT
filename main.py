from fastapi import FastAPI, APIRouter
from fastapi.responses import UJSONResponse
from mangum import Mangum

from api.order import router as order_router

app = FastAPI(default_response_class=UJSONResponse)
api_router = APIRouter(prefix="/api")


@app.get("/healthcheck")
async def health_check():
    return {"message": "OK"}


api_router.include_router(order_router)
app.include_router(api_router)

handler = Mangum(app)