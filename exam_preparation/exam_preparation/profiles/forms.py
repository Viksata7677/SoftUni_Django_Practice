from django import forms

from exam_preparation.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDetailForm(ProfileBaseForm):
    pass