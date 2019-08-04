import os
from pathlib import Path

from arcli.config.base import ROOT_DIR
from arcli.exceptions.base import InvalidArcliFile


class Reader(object):
    def __init__(self, file):
        self.file = self.finder(file)

    @staticmethod
    def finder(file):
        """
        Try to find an arcli file
        :param file: path to arcli file
        :return: Pathlib Path file
        """
        if os.path.exists(os.path.join(os.getcwd(), file)):
            return Path(os.path.join(os.getcwd(), file))
        elif os.path.exists(file):
            return Path(file)
        elif os.path.exists(os.path.join(ROOT_DIR, file)):
            return Path(os.path.join(ROOT_DIR, file))
        else:
            raise InvalidArcliFile("Invalid Arcli file {}".format(file))
