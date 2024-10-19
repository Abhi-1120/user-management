from enum import Enum

__all__ = ["EnvironmentType"]


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"
