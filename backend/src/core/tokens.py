import http

from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from services.auth import AuthService, get_auth_service


async def security_refresh_token(
    refresh_token: str = Depends(APIKeyHeader(name='refresh_token')),
    auth_service: AuthService = Depends(get_auth_service),
):
    """Получаем и проверяем рефреш токен, что не в отозванных"""
    active_refresh_token = await auth_service.get_refresh_token(refresh_token)
    if not active_refresh_token:
        raise HTTPException(
            status_code=http.HTTPStatus.FORBIDDEN,
            detail='Invalid or expired refresh token.',
        )
    return active_refresh_token
