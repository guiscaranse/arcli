import platform

from arcli.triggers.base import ArcliTrigger


class OSCheck(ArcliTrigger):
    """
    This trigger will check if the OS is the same from args
    Example:
          trigger:
            name: OSCheck
            args: ["linux", "windows", "osx"]
    This will check if the host OS is one of the OS on args.
    """

    def run(self, *args, **kwargs) -> bool:
        # Get repo
        for arg in args:
            if str(arg).upper() == str(platform.system()).upper():
                return True
        return False
