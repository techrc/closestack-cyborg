class ModelBase(object):
    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        setattr(self, name, value)
