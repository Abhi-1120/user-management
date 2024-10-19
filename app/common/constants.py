"""API List"""

# Login APIs
LOGIN = "/v1/login"
REFRESH_TOKEN = "/v1/refresh-token"

# Users API
API_V1_CREATE_USER_ENDPOINT = "/v1/user"
API_V1_LIST_USER_ENDPOINT = "/v1/users"
API_V1_GET_USER_ENDPOINT = "/v1/user/{user_id}"
API_V1_UPDATE_USER_ENDPOINT = "/v1/user/{user_id}"
API_V1_BULK_UPDATE_USER_ENDPOINT = "/v1/users"
API_V1_DELETE_USER_ENDPOINT = "/v1/user/{user_id}"
API_V1_USER_MODULE_PERMISSION_CHECK_ENDPOINT = "/v1/user/{user_id}/modules/{module}"


# Roles API
API_V1_CREATE_ROLE_ENDPOINT = "/v1/role"
API_V1_LIST_ROLE_ENDPOINT = "/v1/roles"
API_V1_GET_ROLE_ENDPOINT = "/v1/role/{role_id}"
API_V1_UPDATE_ROLE_ENDPOINT = "/v1/role/{role_id}"
API_V1_DELETE_ROLE_ENDPOINT = "/v1/role/{role_id}"
