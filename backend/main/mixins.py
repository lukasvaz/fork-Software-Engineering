from django.contrib.auth.models import User

class FilterQuerySetMixin():
    queryset_params ={
        'filter':'pk',
        'request_user':'pk'
                      }
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            qs=self.get_serializer().Meta.model.objects.all()
            return qs
        else:
            lookup_data=dict()
            qs=self.get_serializer().Meta.model.objects.all()
            lookup_data[self.queryset_params['filter']]=self.request.user.__getattribute__(self.queryset_params['request_user'])
            return qs.filter(**lookup_data).order_by('pk')