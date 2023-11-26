from django import forms


class DaySelector(forms.Form):

    DAY_OF_WEEK = [
        (0, 'Friday'),
        (1, 'Saturday'),
        (2, 'Sunday'),
    ]

    day = forms.ChoiceField(choices=DAY_OF_WEEK,
                            initial=0,
                            label='',
                            widget=forms.Select(attrs={'class': 'day-selector-dropdown',
                                                       'onchange': 'this.form.submit();'}))
