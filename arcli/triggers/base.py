class ArcliTrigger(object):
    def __init__(self, *args, **kwargs):
        self.run(args, kwargs)

    def run(self, *args, **kwargs) -> bool:
        return True
