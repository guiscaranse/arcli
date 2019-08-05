class ArcliException(BrokenPipeError):
    def __init__(self, message, *args):
        self.message = message
        super(ArcliException, self).__init__(message, *args)


class InvalidArcliFile(ArcliException):
    pass


class InvalidArcliFileContents(ArcliException):
    pass
