from app import router
from app.service import LoginService, GetRefreshedAccessToken
from app.common import (LOGIN, REFRESH_TOKEN, LoginRequestSchema, RefreshTokenSchema)

__all__ = ["login", "get_access_token_using_refresh_token"]


@router.post(LOGIN)
async def login(request: LoginRequestSchema):
    service = LoginService(request)
    response = await service.do_process()
    return response


@router.post(REFRESH_TOKEN)
def get_access_token_using_refresh_token(request: RefreshTokenSchema):
    service = GetRefreshedAccessToken(request)
    response = service.do_process()
    return response
