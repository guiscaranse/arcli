from arcli.shared.util import file_exists
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

    def run(self, *args, **kwargs) -> bool:
        if not args:
            return False
        return all(file_exists(file) for file in args)
