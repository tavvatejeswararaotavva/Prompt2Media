from fastapi import APIRouter, HTTPException
from app.schemas.image_request import GenerateRequest
from app.services import local_diffusion_service, stability_service

router = APIRouter()

@router.post("/generate")
async def generate_media(request: GenerateRequest):
    prompt = request.prompt
    media_type = request.media_type

    if media_type == "image":
        path = local_diffusion_service.generate_image(prompt)
        return {"media_type": "image", "path": path}

    elif media_type == "video":
        path = stability_service.generate_video(prompt)
        return {"media_type": "video", "path": path}

    else:
        raise HTTPException(status_code=400, detail="Invalid media_type")