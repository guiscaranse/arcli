import fnmatch
import os

from git import Repo

from arcli.config.base import SHARED_DB
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
        # Check if is one time
        if kwargs.get("onetime", False):
            db = SHARED_DB
            if db.get("git_last_commit") == str(hcommit):
                return False
            db.add({"git_last_commit": str(hcommit)})
        # Get diffs between last and first
        diffs = hcommit.diff('HEAD~1')
        if args:
            # Use args to find matches
            for arg in args:
                for diff in diffs:
                    if fnmatch.fnmatch(diff.a_path, arg) or fnmatch.fnmatch(diff.b_path, arg):
                        return True
        else:
            if diffs:
                return True
        return False
