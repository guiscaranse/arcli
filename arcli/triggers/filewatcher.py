import os

from arcli.config.base import ROOT_DIR
from arcli.triggers.base import ArcliTrigger


class FileWatcher(ArcliTrigger):
    """
    This trigger will check if a file or directory exists
    Example:
          trigger:
            name: FileWatcher
            args: ["node_modules"]
    This will check if a given file or directory exists.
    If multiple args were given, all files/folders must exist to trigger
    If no argument is provided it will not trigger.
    """
    def file_exists(self, file) -> bool:
        if os.path.exists(file):
            return True
        elif os.path.exists(os.path.join(os.getcwd(), file)):
            return True
        elif os.path.exists(os.path.join(ROOT_DIR, file)):
            return True

    def run(self, *args, **kwargs) -> bool:
        if not args:
            return False
        return all(self.file_exists(file) for file in args)
