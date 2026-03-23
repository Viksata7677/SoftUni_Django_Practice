from django import forms


class PersonForm(forms.Form):
    person_name = forms.CharField()
    age = forms.IntegerField()