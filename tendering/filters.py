import django_filters

from .models import *

class TenderFilter(django_filters.FilterSet):
    

    class Meta:
        model = T_detail
        fields = ['no', 'title', 't_status', 'management', 'owner',]