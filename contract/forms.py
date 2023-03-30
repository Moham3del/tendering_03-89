from django import forms
from django.forms import ModelForm

from .models import *


class Contract_Detail_Form(ModelForm):
    class Meta:
        model = Contract_Detail
        fields = "__all__"



class Action_Form(ModelForm):
    class Meta:
        model = Actions
        fields = "__all__"

class Contract_code_Form(ModelForm):
    class Meta:
        model = Contract_code
        fields = "__all__"

class Sector_Form(ModelForm):
    class Meta:
        model = Sector_manager_action
        fields = "__all__"

class Check_data_Form(ModelForm):
    class Meta:
        model = Check_data_action
        fields = "__all__"

class Cost_estimation_Form(ModelForm):
    class Meta:
        model = Cost_estimation_action
        fields = "__all__"

class Financial_Form(ModelForm):
    class Meta:
        model = Financial_action
        fields = "__all__"

class Copy_contract_Form(ModelForm):
    class Meta:
        model = Copy_contract_action
        fields = "__all__"

class Check_contract_Form(ModelForm):
    class Meta:
        model = Check_contract_action
        fields = "__all__"

class TCTA_Form(ModelForm):
    class Meta:
        model = TCTA_action
        fields = "__all__"

class EVP_Form(ModelForm):
    class Meta:
        model = EVP_action
        fields = "__all__"

class CEO_Form(ModelForm):
    class Meta:
        model = CEO_action
        fields = "__all__"

class Assignmnt_Form(ModelForm):
    class Meta:
        model = Assignmnt_action
        fields = "__all__"
