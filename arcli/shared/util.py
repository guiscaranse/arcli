import os
from pathlib import Path
from typing import Optional

from arcli.config.base import ROOT_DIR


def file_exists(file) -> Optional[Path]:
    if os.path.exists(file):
        return Path(file)
    elif os.path.exists(os.path.join(os.getcwd(), file)):
        return Path(os.path.join(os.getcwd(), file))
    elif os.path.exists(os.path.join(ROOT_DIR, file)):
        return Path(os.path.join(ROOT_DIR, file))
    return None
