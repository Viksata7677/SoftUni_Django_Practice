from django import forms

from forum_app.posts.mixins import DisabledFieldsMixin
from forum_app.posts.models import Post


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


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.NumberInput
        }

        help_text = {
            'title':  'This is the title'
        }

        labels = {
            'title': "That's a label"
        }

        error_messages = {
            'title': {
                'required': 'Enter the title of the post'
            },
            'author': {
                'required': 'Enter an author of the post'
            }
        }


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisabledFieldsMixin):
    disabled_fields = ['title', 'content', 'author', 'languages']