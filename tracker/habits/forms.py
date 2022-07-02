from django import forms

class AddNewSleepEntry(forms.Form):
    note = forms.CharField(max_length=200, label='Add a new sleep entry', required=False)

class AddNewAwakeEntry(forms.Form):
    note = forms.CharField(max_length=200, label='Add a new awake entry', required=False)

class AddNewDipEntry(forms.Form):
    note = forms.CharField(max_length=200, label='Add a new dip entry', required=False)

class AddNewDreamNote(forms.Form):
    note = forms.CharField(max_length=2000, label='Add a new dream note')

class NewNote(forms.Form):
    CHOICES = [
        ('asleep', 'Asleep'),
        ('awake', 'Awake'),
        ('dip', 'Dip')
    ]
    note = forms.CharField(max_length=200, label="Note:")
    type_of_note = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

class AddNewDreamNote(forms.Form):
    note = forms.CharField(max_length=2000, label='Note:')

    def __str__(self):
        return self.note