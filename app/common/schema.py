from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, validator

__all__ = ["LoginRequestSchema", "RefreshTokenSchema", "Token", "CreateUserSchema", "UserQueryParams", "UpdateUserSchema",
           "BulkUserUpdateRequest", "CreateRoleSchema", "RoleQueryParams", "UpdateRoleSchema"]


class BaseResponseSchema(BaseModel):
    ok: bool


class LoginRequestSchema(BaseModel):
    username: str
    password: str


class RefreshTokenSchema(BaseModel):
    token: str


class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
    user_id: int


class CreateUserSchema(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    role: int


class UserQueryParams(BaseModel):
    search: Optional[str] = ""
    limit: Optional[int] = 20
    offset: Optional[int] = Field(1, gt=0, description="offset field")


class UpdateUserSchema(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str = None
    role: int


class UserUpdateSchema(BaseModel):
    user_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[int] = None


class BulkUserUpdateRequest(BaseModel):
    user_data: List[UserUpdateSchema]


class AccessibleModules(BaseModel):
    modules: str


class CreateRoleSchema(BaseModel):
    role_name: str
    access_modules: List[AccessibleModules]
    active: bool

    @validator('access_modules')
    def check_unique_modules(cls, modules: List[AccessibleModules]) -> List[AccessibleModules]:
        module_names = [module.moduleName for module in modules]
        if len(module_names) != len(set(module_names)):
            raise ValueError("Access modules must be unique.")
        return modules


class RoleQueryParams(BaseModel):
    search: Optional[str] = ""
    limit: Optional[int] = 20
    offset: Optional[int] = Field(1, gt=0, description="offset field")


class UpdateRoleSchema(BaseModel):
    role_name: str
    access_modules: List[AccessibleModules]
    active: bool

    @validator('access_modules')
    def check_unique_modules(cls, modules: List[AccessibleModules]) -> List[AccessibleModules]:
        module_names = [module.moduleName for module in modules]
        if len(module_names) != len(set(module_names)):
            raise ValueError("Access modules must be unique.")
        return modules
