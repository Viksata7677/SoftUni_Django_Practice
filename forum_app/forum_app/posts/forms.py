from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forum_app.posts.mixins import DisabledFieldsMixin
from forum_app.posts.models import Post, Comment


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

        # widgets = {
        #     'title': forms.NumberInput
        # }

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

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if author[0] != author[0].upper():
            raise ValidationError('Author name should start with capital letter!')

        return author

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and title in content:
            raise ValidationError('Title cannot be included in the content')

    def save(self, commit=True):
        post = super().save(commit=False)

        post.title = post.title.capitalize()

        if commit:
            post.save()

        return post


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisabledFieldsMixin):
    class Meta(PostBaseForm.Meta):
        exclude = ['image']

    disabled_fields = ['title', 'content', 'author', 'languages']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        labels = {
            'author': '',
            'content': ''
        }
        error_messages = {
            'author': {
                'required': 'Author name is required'
            },
            'content': {
                'required': 'Content is required'
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attr.update({
            'placeholder': 'Your name'
        })

        self.fields['content'].widget.attr.update({
            'placeholder': 'Add message'
        })


CommentFormSet = formset_factory(CommentForm, extra=3)