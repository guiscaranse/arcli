from .always import Always
from .git import GitDiff
from .filewatcher import FileWatcher
from .oscheck import OSCheck

triggers = ["Always", "GitDiff", "FileWatcher", "OSCheck"]

__all__ = triggers
