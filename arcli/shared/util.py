import os

from arcli.config.base import ROOT_DIR


def file_exists(file) -> bool:
    if os.path.exists(file):
        return True
    elif os.path.exists(os.path.join(os.getcwd(), file)):
        return True
    elif os.path.exists(os.path.join(ROOT_DIR, file)):
        return True
