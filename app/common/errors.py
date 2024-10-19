__all__ = ['errors']

errors = {
    "Exception": {
        'ok': False,
        'error': 'INTERNAL_SERVER_ERROR',
        'message': "Oops! Something went wrong. Please try again later.",
        'status': 500
    },
    'InternalServerException': {
        'ok': False,
        'error': 'SERVER_ERROR',
        'message': "Service is down. Please try again after some time!",
        'status': 500
    },
    'BadRequestError': {
        'ok': False,
        'error': 'BAD_REQUEST',
        'message': "",
        'status': 400
    },
    "InvalidUserException": {
        'ok': False,
        'error': 'INVALID_USER_PASSWORD',
        'message': "User is Invalid.",
        'status': 400
    },
    "InvalidPasswordException": {
        'ok': False,
        'error': 'INVALID_USERNAME_PASSWORD',
        'message': "Please check your password. If you still can't log in, contact your administrator.",
        'status': 401
    },
    "UserAlreadyExistException": {
        'ok': False,
        'error': 'USER_ALREADY_EXIST',
        'message': "Oops! A user with the same email already exists in the system.",
        'status': 400
    },
    "UserNotFoundException": {
        'ok': False,
        'error': 'USER_NOT_FOUND',
        'message': "User does not exist in system.",
        'status': 404
    },
    "RoleAlreadyExistException": {
        'ok': False,
        'error': 'ROLE_ALREADY_EXIST',
        'message': "Oops! A role with the same name already exists in the system.",
        'status': 400
    },
    "AccessModuleAlreadyExistException": {
        'ok': False,
        'error': 'ACCESS_MODULE_ALREADY_EXIST',
        'message': "Oops! A access module is already exists for role.",
        'status': 400
    },
    "InvalidTokenException": {
        'ok': False,
        'error': 'INVALID_TOKEN_EXCEPTION',
        'message': "Provided token is invalid.",
        'status': 401
    },
    "RoleNotFoundException": {
        'ok': False,
        'error': 'ROLE_NOT_FOUND',
        'message': "Role does not exist in system.",
        'status': 404
    }
}
