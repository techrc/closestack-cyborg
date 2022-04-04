class VersionedObject(object):
    def __init__(self, **kwargs):
        self._changed_fields = set()
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def obj_reset_changes(self):
        self._changed_fields.clear()


class VersionedObjectDictCompat(object):
    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        setattr(self, name, value)
