from fastapi import APIRouter
from pydantic import BaseModel
import openai

router = APIRouter(prefix="/dall-e", tags=["dall-e"])
metadata_order = {
    "name": "Dall-E API Version 1",
    "description": "Version 1 Dall-E API"
}


class Item(BaseModel):
    description: str
    numbers: int


@router.post(
    path="", summary="POST Dall-E images"
)
async def generate_images(item: Item):
    openai.api_key = "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"
    response = openai.Image.create(
        prompt=item.description,
        n=item.numbers,
        size="1024x1024"
    )
    return response
