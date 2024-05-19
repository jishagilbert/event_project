from django import forms

from evenapp.models import Booking, Review


class registrationForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

class ReviewForm(forms.ModelForm):
     class Meta:
         model = Review
         fields = ['name', 'comment', 'rating']

