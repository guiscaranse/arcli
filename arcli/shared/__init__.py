from pickledb import PickleDB


class SharedDB(PickleDB):
    def __init__(self, location, auto_dump, sig=True):
        super().__init__(location, auto_dump, sig)

    def get(self, key):
        if self.dexists("shared", key):
            return self.dget("shared", key)
        else:
            return ""

    def add(self, pair: dict):
        for key, value in pair.items():
            self.db["shared"][key] = value
            self._autodumpdb()
        return True