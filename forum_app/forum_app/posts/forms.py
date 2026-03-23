from django import forms


class PersonForm(forms.Form):
    STATUS_CHOICE = (
        (1, 'Draft'),
        (2, 'Published'),
        (3, 'Archived')
    )

    person_name = forms.CharField(label="Add person's name", widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    age = forms.IntegerField()
    date = forms.DateField()
    is_lecturer = forms.BooleanField()
    status = forms.IntegerField(widget=forms.Select(choices=STATUS_CHOICE))