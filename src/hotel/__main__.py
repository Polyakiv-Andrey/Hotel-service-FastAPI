import uvicorn

from src.hotel.settings import settings

uvicorn.run(
    "hotel.app:app",
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)
