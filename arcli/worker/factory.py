import subprocess

from arcli.exceptions.base import InvalidRuntimeCommand
from arcli.worker.models import ArcliStep
from arcli.worker.reader import Reader


class Factory(object):
    def __init__(self, reader: Reader):
        self.reader = reader

    def run(self):
        # get data
        data = self.reader.get_model()
        # get each command
        for run in data.runtime:
            # check if it is a step
            if isinstance(run, ArcliStep):
                # check if trigger exists and is triggered
                if run.trigger and not run.trigger.obj.run(*run.trigger.args, **run.trigger.options):
                    continue
                # get script from step
                run = run.script

            # start command exec
            try:
                # check if is a single command
                if isinstance(run, str):
                    subprocess.run(str(run).split(" "), check=True)
                else:  # probably a list
                    for c in run:
                        subprocess.run(str(c).split(" "), check=True)
            except Exception as e:
                # get errors on runtime
                raise InvalidRuntimeCommand(e.__str__())
