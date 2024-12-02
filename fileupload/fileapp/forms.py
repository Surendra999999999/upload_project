from django import forms
from .models import MediaFiles
class MediaFileForm(forms.ModelForm):
    class Meta:
        model=MediaFiles
        fields=['title','file']
    