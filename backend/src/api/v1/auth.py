from http import HTTPStatus

from fastapi import APIRouter, Response
from schemas.entity import UserCreate, UserInDB, UserSignIn

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
):
    pass

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
):
    pass