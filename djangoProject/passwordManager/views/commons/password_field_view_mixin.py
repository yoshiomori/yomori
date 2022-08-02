from django.forms import PasswordInput


class PasswordFieldViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget = PasswordInput(attrs=form.fields['password'].widget.attrs, render_value=True)
        return form