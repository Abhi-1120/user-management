from app import router
from fastapi import Depends
from app.service import (CreateUserService, UserListService, GetUserService, UpdateUserService, BulkUpdateUserService,
                         DeleteUserService, UserModuleAccessService)
from app.common import (API_V1_CREATE_USER_ENDPOINT, API_V1_LIST_USER_ENDPOINT, API_V1_GET_USER_ENDPOINT,
                        API_V1_UPDATE_USER_ENDPOINT, API_V1_BULK_UPDATE_USER_ENDPOINT, API_V1_DELETE_USER_ENDPOINT,
                        API_V1_USER_MODULE_PERMISSION_CHECK_ENDPOINT, CreateUserSchema, UserQueryParams,
                        BulkUserUpdateRequest, UpdateUserSchema)

__all__ = ["create_user", "users_list", "get_user", "update_user", "bulk_update_user", "delete_user"]


@router.post(API_V1_CREATE_USER_ENDPOINT)
async def create_user(request: CreateUserSchema):
    service = CreateUserService(request)
    response = await service.create_user()
    return response


@router.get(API_V1_LIST_USER_ENDPOINT)
async def users_list(query_params: UserQueryParams = Depends()):
    service = UserListService(query_params)
    response = await service.users_list()
    return response


@router.get(API_V1_GET_USER_ENDPOINT)
async def get_user(user_id: int):
    service = GetUserService(user_id)
    response = await service.get_user()
    return response


@router.put(API_V1_UPDATE_USER_ENDPOINT)
async def update_user(user_id: int, request: UpdateUserSchema):
    service = UpdateUserService(user_id, request)
    response = await service.update_user()
    return response


@router.put(API_V1_BULK_UPDATE_USER_ENDPOINT)
async def bulk_update_user(request: BulkUserUpdateRequest):
    service = BulkUpdateUserService(request)
    response = await service.bulk_update_user()
    return response


@router.delete(API_V1_DELETE_USER_ENDPOINT)
async def delete_user(user_id: int):
    service = DeleteUserService(user_id)
    response = await service.delete_user()
    return response


@router.get(API_V1_USER_MODULE_PERMISSION_CHECK_ENDPOINT)
async def validate_user_module_access(user_id: int, module_name: str):
    service = UserModuleAccessService(user_id, module_name)
    response = await service.validate_user_module_access()
    return response
