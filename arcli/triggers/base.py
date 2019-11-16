class ArcliTrigger(object):
    """
        Base class for triggers.
        Each trigger will be run through the run method, if it returns True, trigger will run it
        attached commands on runtime.
    """
    def __init__(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs) -> bool:
        return True
