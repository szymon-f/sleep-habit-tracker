from django import forms

class AddNewSleepEntry(forms.Form):
    note = forms.CharField(max_length=200, label='Add a new sleep entry', required=False)