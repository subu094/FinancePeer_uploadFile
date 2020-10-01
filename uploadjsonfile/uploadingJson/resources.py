from import_export import resources
from .models import JsonDatas

class JsonResources(resources.ModelResource):
    class Meta:
        model = JsonDatas

# class PersonResource(resources.ModelResource):
#     class Meta:
#         model = Person