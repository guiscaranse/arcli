import os
from pathlib import Path

import yaml

from arcli.config.base import ROOT_DIR
from arcli.exceptions.base import InvalidArcliFile
from arcli.worker.models import ArcliFile
from arcli.worker.models.parsers import build_runtime


class Reader(object):
    def __init__(self, file, key_reader="runtime"):
        self.file = self.finder(file)
        self.data = self.parse()
        self.model = self.model_validate(runtime_key=key_reader)

    @staticmethod
    def finder(file):
        """
        Try to find an arcli file
        :param file: path to arcli file
        :return: Pathlib Path file
        """
        if os.path.exists(file):
            return Path(file)
        elif os.path.exists(os.path.join(os.getcwd(), file)):
            return Path(os.path.join(os.getcwd(), file))
        elif os.path.exists(os.path.join(ROOT_DIR, file)):
            return Path(os.path.join(ROOT_DIR, file))
        else:
            raise InvalidArcliFile("Invalid Arcli file {}".format(file))

    def parse(self) -> dict:
        """
        Parse file to PyYAML
        :return:
        """
        try:
            from yaml import CLoader as Loader, CDumper as Dumper
        except ImportError:
            from yaml import Loader, Dumper
        return yaml.load(self.file.read_text(), Loader=Loader)

    def model_validate(self, runtime_key) -> ArcliFile:
        """
        Create and fill model, this will translate YAML to Pydantic
        :return: ArcliFile (Pydantic Model)
        """
        runtime = build_runtime(self.data, key=runtime_key)
        # We will always want to remove runtime
        self.data.pop("runtime", runtime_key)
        return ArcliFile(**self.data, runtime=runtime)

    def get_model(self):
        return self.model