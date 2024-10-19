from app import router
from fastapi import Depends
from app.service import (CreateRoleService, RoleListService, GetRoleService, UpdateRoleService,
                         DeleteRoleService)
from app.common import (API_V1_CREATE_ROLE_ENDPOINT, API_V1_LIST_ROLE_ENDPOINT, API_V1_GET_ROLE_ENDPOINT,
                        API_V1_UPDATE_ROLE_ENDPOINT, API_V1_DELETE_ROLE_ENDPOINT,
                        CreateRoleSchema, RoleQueryParams, UpdateRoleSchema)

__all__ = ["create_role", "roles_list", "get_role", "update_role", "delete_role"]


@router.post(API_V1_CREATE_ROLE_ENDPOINT)
async def create_role(request: CreateRoleSchema):
    service = CreateRoleService(request)
    response = await service.create_role()
    return response


@router.get(API_V1_LIST_ROLE_ENDPOINT)
async def roles_list(query_params: RoleQueryParams = Depends()):
    service = RoleListService(query_params)
    response = await service.roles_list()
    return response


@router.get(API_V1_GET_ROLE_ENDPOINT)
async def get_role(role_id: int):
    service = GetRoleService(role_id)
    response = await service.get_role()
    return response


@router.put(API_V1_UPDATE_ROLE_ENDPOINT)
async def update_role(role_id: int, request: UpdateRoleSchema):
    service = UpdateRoleService(role_id, request)
    response = await service.update_role()
    return response


@router.delete(API_V1_DELETE_ROLE_ENDPOINT)
async def delete_role(role_id: int):
    service = DeleteRoleService(role_id)
    response = await service.delete_role()
    return response
