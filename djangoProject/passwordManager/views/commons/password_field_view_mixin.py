from django.forms import PasswordInput


class PasswordFieldViewMixin:
    """O Widget password gerado no servidor, permite que o input do HTML seja do tipo password mesmo quando o
     javascript esteja desabilitado"""
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget = PasswordInput(attrs=form.fields['password'].widget.attrs, render_value=True)
        return form
