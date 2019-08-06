import fnmatch
import os

from git import Repo

from arcli.triggers.base import ArcliTrigger


class GitDiff(ArcliTrigger):
    """
    This trigger will check difference in files in a Git repo.
    Example:
          trigger:
            name: GitDiff
            args: ["docker-compose.yml", "arcli/*.py]
    This will check if the difference between the current and last commit was with those files.
    If no argument is provided it will check if there where differences (will in most cases, always trigger).
    """
    def run(self, *args, **kwargs) -> bool:
        # Get repo
        repo = Repo(os.getcwd())
        if not repo:
            return False
        # Get last commit
        hcommit = repo.head.commit
        # Get diffs between last and first
        diffs = hcommit.diff('HEAD~1')
        if args:
            # Use args to find matches
            for arg in args:
                for diff in diffs:
                    if fnmatch.fnmatch(arg, diff.a_path) or fnmatch.fnmatch(arg, diff.b_path):
                        return True
        else:
            if diffs:
                return True
        return False
