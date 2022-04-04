from cslo_versionedobjects import base as object_base
from pecan import request

from cyborg.objects import base


class Device(base.CyborgObject, object_base.VersionedObjectDictCompat):
    fields = ['id', 'uuid']
    

    @classmethod
    def list(cls, filters=None):
        dbapi = request.db_conn
        db_devices = dbapi.device_list()
        return cls._from_db_obj_list(db_devices)

    def save(self):
        ...

    def create(self):
        ...

    def destroy(self):
        ...

