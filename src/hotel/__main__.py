import uvicorn

uvicorn.run(
    "hotel.app:app",
    reload=True
)
