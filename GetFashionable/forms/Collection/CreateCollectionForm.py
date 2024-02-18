from django import forms

from ...models import Collection, Design
from ...forms import CreateDesignForm


# Is needed to create a formset for the designs in the collection form
# In this form uses can create a collection and add designs to it
DesignFormSet = forms.inlineformset_factory(
    Collection,
    Design,
    form=CreateDesignForm,
    extra=1,
    can_delete=False
)


class CreateCollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = ['name', 'description']
