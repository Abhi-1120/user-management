from builtins import Exception

__all__ = ["GeneralException", 'BadRequestError', "InternalServerException", "InvalidUserException",
           "InvalidPasswordException", "UserAlreadyExistException", "UserNotFoundException", "RoleNotFoundException",
           "RoleAlreadyExistException", "AccessModuleAlreadyExistException", "InvalidTokenException"]


class GeneralException(Exception):
    pass


class InternalServerException(GeneralException):
    pass


class BadRequestError(GeneralException):
    pass


class InvalidUserException(GeneralException):
    pass


class InvalidPasswordException(GeneralException):
    pass


class UserAlreadyExistException(GeneralException):
    pass


class UserNotFoundException(GeneralException):
    pass


class RoleAlreadyExistException(GeneralException):
    pass


class RoleNotFoundException(GeneralException):
    pass


class AccessModuleAlreadyExistException(GeneralException):
    pass


class InvalidTokenException(GeneralException):
    pass
