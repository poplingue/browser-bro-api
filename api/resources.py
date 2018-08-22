from tastypie.resources import ModelResource
from api.models import Custom
from tastypie.authorization import Authorization

class CustomResource(ModelResource):
    class Meta:
        queryset = Custom.objects.all()
        resource_name = 'customs'
        authorization = Authorization()
