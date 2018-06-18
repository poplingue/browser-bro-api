from tastypie.resources import ModelResource
from api.models import Custom

class CustomResource(ModelResource):
    class Meta:
        queryset = Custom.objects.all()
        resource_name = 'customs'
