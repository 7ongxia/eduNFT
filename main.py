from fastapi import FastAPI, APIRouter
from mangum import Mangum

from api.ipfs import router as ipfs_router
from api.dalle import router as dalle_router

app = FastAPI()
api_router = APIRouter(prefix="/api")


@app.get("/healthcheck")
async def health_check():
    return {"message": "OK"}


api_router.include_router(ipfs_router)
api_router.include_router(dalle_router)
app.include_router(api_router)

handler = Mangum(app)