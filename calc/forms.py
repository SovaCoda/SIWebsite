from django import forms

class NameForm(forms.Form):
    your_text = forms.CharField(label='', max_length = 100000,
        widget=forms.Textarea(attrs={'rows':'35','cols':'70', 'style':'resize:none;'}))