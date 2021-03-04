from django import forms
from .models import Timer


class TimerForm(forms.Form):

    start = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'time_set',
            'value': 'time_set'
        }
    ), required=True)
    end = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'time_stop',
            'readonly': True
        }
    ), required=False)

    def clean(self):
        cd = super(TimerForm, self).clean()
        start = cd.get('start')
        end = cd.get('end')

        return cd
