from typing import Union

import pkg_resources
from pydantic import BaseModel, validator
from semantic_version import Spec, Version

from arcli.exceptions.base import InvalidArcliFileContents


class ArcliFile(BaseModel):
    arcli: Union[str, float]  # Arcli Version

    @validator('arcli')
    def check_arcli_version(cls, arcli):
        current_version = pkg_resources.get_distribution('arcli').version
        required_version = Spec(arcli)
        if not required_version.match(Version(current_version)):
            raise InvalidArcliFileContents('Invalid Arcli version for this project. '
                                           '(Installed {}, Required {})'.format(current_version, required_version))
        return current_version
