from django import forms


def register():
    name = forms.CharField(label="name",max_length=100)
    