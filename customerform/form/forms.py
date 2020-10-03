from django import forms
from .models import BlogData

class BlogForm(forms.ModelForm):
	class Meta():
		model = BlogData
		fields = ('Title','Description','Image','Hashtag')