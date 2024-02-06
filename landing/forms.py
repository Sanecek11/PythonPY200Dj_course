from django import forms


class TemplateForm(forms.Form):
    name = forms.CharField()
    # choices в ChoiceField нужен только для отображения в HTML форме
    # widget тоже нужен только для отображения в HTML
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

