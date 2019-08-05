import platform
from typing import Union, Optional, List

import pkg_resources
from pydantic import BaseModel, validator
from semantic_version import Spec, Version

from arcli.exceptions.base import InvalidArcliFileContents
from arcli.worker.models.enum import OSEnum
from arcli.worker.models.util import is_tool


class ArcliStepTrigger(BaseModel):
    name: str
    args: List[str] = []


class ArcliStep(BaseModel):
    name: str
    trigger: Optional[ArcliStepTrigger] = None
    script: list = []


class ArcliFile(BaseModel):
    arcli: Union[str, float]  # Arcli Version
    os: OSEnum = OSEnum.any
    env: List[str] = []
    dependencies: List[str] = []
    runtime: Union[List[str], ArcliStep] = []

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
        if not str(os.value).upper() == str(platform.system()).upper() and os != OSEnum.any:
            raise InvalidArcliFileContents('Invalid operational system.')
        return os

    @validator('dependencies')
    def check_dependencies(cls, dep):
        if not is_tool(dep):
            raise InvalidArcliFileContents('Required dependency is missing or is not in PATH ({}).'.format(dep))
        return dep
