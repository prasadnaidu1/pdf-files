from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(
        label='Enter Your First Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':"Your First Name"
            }
        )
    )
    lastname = forms.CharField(
        label='Enter Your Last Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':"Your Last Name"
            }
        )
    )
    email = forms.EmailField(
        label='Enter Your Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':"Your Email"
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':"Your Mobile Number"
            }
        )
    )


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )

    rating = forms.IntegerField(
        label='Enter Rating:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label='Enter Your Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )

















