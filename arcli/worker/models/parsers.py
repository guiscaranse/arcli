from arcli.worker.models import ArcliStep, ArcliStepTrigger


def build_runtime(data: dict) -> list:
    runtime = []
    for key in data['runtime']:
        if isinstance(key, str) and "$step" in key:
            name = key.split(" ", 1)[1]
            step_desc = data.get("step @{}".format(name))
            if step_desc:
                step_trigger = None
                if 'trigger' in step_desc.keys():
                    step_trigger = ArcliStepTrigger(name=step_desc['trigger']['name'],
                                                    args=step_desc['trigger'].get("args", []),
                                                    options=step_desc['trigger'].get("options", {}))
                runtime.append(ArcliStep(name=name, script=step_desc.get('script', []), trigger=step_trigger))
                continue
        runtime.append(key)
    return runtime
