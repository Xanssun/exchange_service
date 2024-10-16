import uvicorn
from core.settings import settings
from db import redis
from db.postgres import async_session
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from redis.asyncio import Redis
from sqlalchemy import text

app = FastAPI(
    title='Messager API',
    docs_url='/mess_api/openapi',
    openapi_url='/mess_api/openapi.json',
    default_response_class=JSONResponse,
)


# Проверка подключения к PostgreSQL
@app.get("/postgres_health")
async def check_postgres():
    """Проверка соеденения, тестовая функция"""
    async with async_session() as session:
        try:
            await session.execute(text("SELECT 1"))
            return {"Соединение с базой данных установлено!"}
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": f"Ошибка подключения к базе данных: {str(e)}"})


if __name__ == '__main__':
    redis.redis = Redis(host=settings.redis_host, port=settings.redis_port)

    uvicorn.run(
        'main:app',
        host=settings.mess_api_host,
        port=settings.mess_api_port,
        reload=True,
    )
