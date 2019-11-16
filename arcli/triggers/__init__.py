from .always import Always
from .git import GitDiff
from .filewatcher import FileWatcher

triggers = ["Always", "GitDiff", "FileWatcher"]

__all__ = triggers
