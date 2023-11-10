from django import forms

from ...models import Design


class CreateDesignForm(forms.ModelForm):

    class Meta:
        model = Design
        fields = ['name', 'image']
