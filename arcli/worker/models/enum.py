from enum import Enum


class OSEnum(str, Enum):
    osx = 'darwin'
    windows = 'windows'
    linux = 'linux'
    any = 'any'
