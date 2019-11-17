from django import forms


class DestinationForm(forms.Form):
    destinationSystem = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control typeahead',
               'placeholder': 'Destination',
               'id': 'destinationInput'}
    )
    )


class DestinationButton(forms.Form):
    destinationSystem = forms.CharField(label='', widget=forms.TextInput(
        attrs={'type': 'hidden',
               'id': 'destinationButton'}
    )
    )
