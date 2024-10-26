import uvicorn
from api.v1 import auth
from core.settings import settings
from db import redis
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from redis.asyncio import Redis
from tools.health import router as health_router

app = FastAPI(
    title='Messager API',
    docs_url='/mess_api/openapi',
    openapi_url='/mess_api/openapi.json',
    default_response_class=JSONResponse,
)

# Подключение маршрутизаторов
app.include_router(auth.router, prefix='/mess_api/v1/auth', tags=['auth'])
app.include_router(health_router)

@app.on_event("startup")
async def startup_event():
    redis.redis = Redis(host=settings.redis_host, port=settings.redis_port)
    await redis.redis.ping()  # Проверка соединения



if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.mess_api_host,
        port=settings.mess_api_port,
        reload=True,
    )
