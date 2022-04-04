from cslo_versionedobjects import base as object_base


class CyborgObject(object_base.VersionedObject):
    fields = ['created_at', 'updated_at']

    def as_dict(self):
        return {k: getattr(self, k) for k in self.fields}

    @classmethod
    def _from_db_obj_list(cls, db_objs):
        objs = []
        for db_obj in db_objs:
            obj = cls()
            objs.append(cls._from_db_obj(obj, db_obj))
        return objs

    @classmethod
    def _from_db_obj(cls, obj, db_obj):
        for field in obj.fields:
            obj[field] = db_obj[field]
        obj.obj_reset_changes()
        return obj

