from pecan import rest
from wsme import types as wtypes
from cyborg.api import expose

from cyborg import objects


class Device(wtypes.Base):
    id = int
    uuid = wtypes.text

    def __init__(self, **kwargs):
        super(Device, self).__init__(**kwargs)
        self.fields = []
        for field in objects.Device.fields:
            self.fields.append(field)
            setattr(self, field, kwargs.get(field, wtypes.Unset))

    @classmethod
    def convert_with_links(cls, obj_device):
        api_device = cls(**obj_device.as_dict())
        # api_device.links = []
        return api_device


class DevicesCollection(wtypes.Base):
    devices = [Device]

    @classmethod
    def convert_with_links(cls, devices):
        collection = cls()
        collection.devices = [Device.convert_with_links(device)
                              for device in devices]
        return collection


class DevicesController(rest.RestController):

    @expose.expose(DevicesCollection)
    def get_all(self):
        obj_devices = objects.Device.list()
        return DevicesCollection.convert_with_links(obj_devices)
        
