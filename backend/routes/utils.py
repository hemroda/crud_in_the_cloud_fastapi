from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["Utils"],)


@router.get("/dismiss-notification", response_class=HTMLResponse)
async def dismiss_notification():
    return Response(content="", media_type="text/html")
