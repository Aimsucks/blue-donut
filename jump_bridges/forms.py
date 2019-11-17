from django import forms


class JumpBridgeForm(forms.Form):
    jumpBridges = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
