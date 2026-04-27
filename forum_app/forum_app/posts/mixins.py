from datetime import time


from django import forms
from django.http import HttpResponseForbidden
from django.utils.timezone import localtime


class DisabledFieldsMixin(forms.Form):
    disabled_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name in self.disabled_fields:
                field.disabled = True


class TimeRestrictedMixin:
    start_time = time(9, 0)
    end_time = time(23, 0)
    forbidden_message = "You don't have access at this time!"

    def dispatch(self, request, *args, **kwargs):
        current_time = localtime().time()

        if not (self.start_time <= current_time <= self.end_time):
            return HttpResponseForbidden(self.forbidden_message)

        return super().dispatch(request, request, *args, **kwargs)