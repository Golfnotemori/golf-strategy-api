from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import StreamingResponse
from strategy import generate_strategy_image

app = FastAPI()

@app.post("/generate")
async def generate(image: UploadFile, distance: float = Form(...), deviation: float = Form(...)):
    image_data = await image.read()
    result_image = generate_strategy_image(image_data, distance, deviation)
    return StreamingResponse(result_image, media_type="image/png")
