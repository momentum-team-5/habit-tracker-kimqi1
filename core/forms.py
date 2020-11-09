from django import forms

from .models import Habit, Record

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('verb', 'goal', 'noun',)


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('habit', 'date', 'number',)
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date'})
        }