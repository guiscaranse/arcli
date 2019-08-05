def parse_arcli_version(version):
    if isinstance(version, float):
        return "=={}".format(fixes_decimal_places(version))
    else:
        valid = ['<', '>', '==', '<=', '>=', '!=']
        if any(ext in version for ext in valid):
            return fixes_decimal_places(version)
        else:
            return "=={}".format(fixes_decimal_places(version))


def fixes_decimal_places(version):
    if len(str(version).split(".")) > 2:
        return "{}".format(str(version))
    else:
        return "{}".format(str(version) + ".0")
