from django import forms
from polls.models import hardwareImages


class register(forms.Form):
    name = forms.CharField(label="name",max_length=100)
    

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = hardwareImages
        fields = ['GereedschapImage']