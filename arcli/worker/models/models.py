from typing import Union

import pkg_resources
import semver
from pydantic import BaseModel, validator

from arcli.exceptions.base import InvalidArcliFileContents
from arcli.worker.models.util import parse_arcli_version


class ArcliFile(BaseModel):
    arcli: Union[str, float]  # Arcli Version

    @validator('arcli')
    def check_arcli_version(cls, arcli):
        current_version = pkg_resources.get_distribution('arcli').version
        required_version = parse_arcli_version(arcli)
        if not semver.match(current_version, required_version):
            raise InvalidArcliFileContents('Invalid Arcli version for this project. '
                                           '(Installed {}, Required {})'.format(current_version, required_version))
        return required_version
