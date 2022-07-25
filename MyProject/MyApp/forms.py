# forms.py
from django import forms
from .models import *

class FaviconForm(forms.ModelForm):

	class Meta:
		model = Favicon
		fields = ['name', 'icon_Img']
