from django import forms
from django.forms import ModelForm

from .models import T_detail


class T_detail_Form(ModelForm):
    class Meta:
        model = T_detail
        fields = "__all__"
