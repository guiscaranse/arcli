import fnmatch
import os

from git import Repo

from arcli.triggers.base import ArcliTrigger


class GitDiff(ArcliTrigger):
    def run(self, *args, **kwargs) -> bool:
        repo = Repo(os.getcwd())
        if not repo:
            return False
        hcommit = repo.head.commit
        diffs = hcommit.diff('HEAD~1')
        if args:
            for arg in args:
                for diff in diffs:
                    if fnmatch.fnmatch(arg, diff.a_path) or fnmatch.fnmatch(arg, diff.b_path):
                        return True
        else:
            if diffs:
                return True
        return False
