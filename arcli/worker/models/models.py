import platform
from typing import Union

import pkg_resources
from pydantic import BaseModel, validator
from semantic_version import Spec, Version

from arcli.exceptions.base import InvalidArcliFileContents
from arcli.worker.models.enum import OSEnum


class ArcliFile(BaseModel):
    arcli: Union[str, float]  # Arcli Version
    os: OSEnum = OSEnum.any
    dependencies: list = []

    @validator('arcli')
    def check_arcli_version(cls, arcli):
        current_version = pkg_resources.get_distribution('arcli').version
        required_version = Spec(arcli)
        if not required_version.match(Version(current_version)):
            raise InvalidArcliFileContents('Invalid Arcli version for this project. '
                                           '(Installed {}, Required {})'.format(current_version, required_version))
        return current_version

    @validator('os')
    def check_os(cls, os):
        if not str(os).upper() == str(platform.system()).upper() and str(os).upper() != OSEnum.any.upper():
            raise InvalidArcliFileContents('Invalid operational system.')
        return os