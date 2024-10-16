from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from schemas.entity import UserCreate, UserInDB, UserSignIn
from services.auth import AuthService, get_auth_service

router = APIRouter()


@router.post(
    '/signup',
    response_model=UserInDB,
    status_code=HTTPStatus.CREATED,
    summary='Регистрация пользователя',
    description='Регистрация пользователя',
)
async def singup(
    user_create: UserCreate,
    auth_service: AuthService = Depends(get_auth_service),
):
    user = await auth_service.signup(user_create)
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Already exists user with such email',
        )
    return user

@router.post(
    '/signin',
    response_model=UserInDB,
    status_code=HTTPStatus.CREATED,
    summary='Вход пользователя',
    description='Вход пользователя',
)
async def signin(
    response: Response,
    user_signin: UserSignIn,
    auth_service: AuthService = Depends(get_auth_service),
):
    pass


@router.post(
    '/refresh_token',
    response_model=UserInDB,
    status_code=HTTPStatus.OK,
    summary='Обновить токен',
    description='Обновить токен',
)
async def refresh_token(
    response: Response,
    auth_service: AuthService = Depends(get_auth_service),
):
    pass