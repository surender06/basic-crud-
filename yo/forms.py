from django import forms
from .models import Yoga

class YogaForm(forms.ModelForm):
    class Meta:
        model=Yoga
        fields=['name','age','address','image']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form_control',
                'placeholder':'Enter your name',
                'required': True,
                'id':'name'

            }),
            'age':forms.NumberInput(attrs={
                'class':'form_control',
                'placeholder':' Enter your age ',
                'required': True,
                'id':'age',
                }),
            'address':forms.Textarea(attrs={
                'class':'form_control',
                'placeholder':'Enter your address'
            })
        }
    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age < 18:
            raise forms.ValidationError("Age must be 18+")

        return age