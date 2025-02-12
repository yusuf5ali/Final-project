from django import forms

class PredictionForm(forms.Form):
    hp = forms.FloatField(label='Horsepower')
    wt = forms.FloatField(label='Weight (1000 lbs)')
    cyl = forms.IntegerField(label='Number of Cylinders')