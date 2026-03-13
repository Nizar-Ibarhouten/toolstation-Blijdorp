from django import forms


class register(forms.Form):
    name = forms.CharField(label="name",max_length=100)
    
