from __future__ import unicode_literals
from django.contrib.gis.serializers.geojson import Serializer as GeoJSONSerializer


class Serializer(GeoJSONSerializer):
    def get_dump_object(self, obj):
        data = super(Serializer, self).get_dump_object(obj)
        # Extend to your taste
        data.update(id=obj.pk)
        # data.update(status='none')
        # data.update(progress=obj.site_progress)
        return data