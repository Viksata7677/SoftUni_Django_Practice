from django import forms

from exam_preparation.album.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']


class AlbumCreateForm(AlbumBaseForm):
    class Meta(AlbumBaseForm.Meta):
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album name'},),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price'})
        }


class AlbumDeleteForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass