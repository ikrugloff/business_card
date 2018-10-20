from django import forms

from .models import Picture


class AddNewPicForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Picture name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Small description'}), required=False)

    class Meta:
        model = Picture
        fields = ('name', 'description', 'img', 'file')
