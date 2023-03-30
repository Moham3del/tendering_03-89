import django_filters

from .models import *

class ContractFilter(django_filters.FilterSet):
    

    class Meta:
        model = Contract_Detail
        fields = {
            'id': ['exact'], 
            'works_type': ['exact', 'contains'], 
            'sector': ['exact', 'contains'], 
            'creator': ['exact', 'contains'], 
            'secondParty_name': ['exact', 'contains'],
            'sgnllast_status_action': ['exact', 'contains'],
            'contract_no': ['exact'],
            'contract_year': ['exact'],
                  }