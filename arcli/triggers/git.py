import os

from git import Repo

from arcli.triggers.base import ArcliTrigger


class GitDiff(ArcliTrigger):
    def run(self, *args, **kwargs) -> bool:
        repo = Repo(os.getcwd())
        hcommit = repo.head.commit

        print(hcommit.diff('HEAD~1'))
        if not repo:
            return False
        return True
