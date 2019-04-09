from django import forms

class RestaurantCreateview(forms.Form):
    name            = forms.CharField()
    location        = forms.CharField(required=False)
    category        = forms.CharField(required=False)

    def clean_name(self):
        name=self.cleaned_data.get("name")
        if name=="hello":
            raise forms.ValidationError("not a valid name")
        return name
