from django import forms
class uploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class' : 'upload-file'}))