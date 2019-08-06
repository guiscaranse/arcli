import os
import platform
from typing import Union, Optional, List, Any, Dict

import pkg_resources
from pydantic import BaseModel, validator
from semantic_version import Spec, Version

from arcli import triggers
from arcli.exceptions.base import InvalidArcliFileContents, InvalidTrigger
from arcli.triggers.base import ArcliTrigger
from arcli.worker.models.enum import OSEnum
from arcli.worker.models.util import is_tool


class ArcliStepTrigger(BaseModel):
    """
    Model for storing Trigger data
    """
    name: str
    args: List[str] = []
    options: Dict = dict()
    obj: Optional[ArcliTrigger] = None

    @validator('obj', pre=True, always=True, whole=True)
    def check_trigger(cls, value, values):
        if values['name'] not in triggers.__all__:
            raise InvalidTrigger('Invalid trigger ({}).'.format(values['name']))
        obj_class = eval('triggers.{}()'.format(values['name']))
        return obj_class

    class Config:
        arbitrary_types_allowed = True


class ArcliStep(BaseModel):
    """
    Model for storing Step data
    """
    name: str
    trigger: Optional[ArcliStepTrigger] = None
    script: list = []


class ArcliFile(BaseModel):
    """
    arcli.yml will be translated to this model.
    """
    arcli: Union[str, float]  # Arcli Version
    os: OSEnum = OSEnum.any
    env: List[str] = []
    dependencies: List[str] = []
    runtime: List[Union[str, ArcliStep]] = []

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

    @validator('env')
    def check_env(cls, env):
        os.environ[str(env).split("=", 1)[0]] = str(env).split("=", 1)[1]
        return env