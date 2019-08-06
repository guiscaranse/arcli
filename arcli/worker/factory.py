import subprocess

from arcli.exceptions.base import InvalidRuntimeCommand
from arcli.worker.models import ArcliStep
from arcli.worker.reader import Reader


class Factory(object):
    def __init__(self, reader: Reader):
        self.reader = reader

    def run(self):
        data = self.reader.get_model()
        for run in data.runtime:
            if isinstance(run, ArcliStep):
                if not run.trigger or not run.trigger.obj.run(*run.trigger.args):
                    continue
                run = run.script
            try:
                cmd = str(run).split(" ") if isinstance(run, str) else run
                if cmd:
                    subprocess.run(cmd, check=True)
            except Exception as e:
                raise InvalidRuntimeCommand(e.__str__())
