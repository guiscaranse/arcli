def parse_arcli_version(version):
    if isinstance(version, float):
        if len(str(version).split(".")) > 2:
            return "=={}".format(str(version))
        else:
            return "=={}".format(str(version) + ".0")
    else:
        valid = ['<', '>', '==', '<=', '>=', '!=']
        if any(ext in version for ext in valid):
            return version
        else:
            return "=={}".format(version)
