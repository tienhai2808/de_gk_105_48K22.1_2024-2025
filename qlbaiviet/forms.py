from django import forms
from .models import *

class BaiVietForm(forms.ModelForm):
  class Meta:
    model = BaiViet
    exclude = ('nguoi_tao',)