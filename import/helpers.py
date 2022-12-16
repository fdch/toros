import datetime

__ALL__ = ["datefromiso", "datefromtimestamp", "iso"]


def iso(value):
    return str((value).strftime("%Y-%m-%d %H:%M:%S"))


def datefromiso(value):
    if not value:
        return
    return iso(datetime.datetime.fromisoformat(value))


def datefromtimestamp(value):
    # TODO: this does not seem to be accurate because there are
    # repeated dates in the db...
    if not value:
        return
    return iso(
        datetime.datetime.fromtimestamp(0) + datetime.timedelta(milliseconds=value)
    )
