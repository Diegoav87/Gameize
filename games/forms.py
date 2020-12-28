from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'short_description', 'description', 'cover_image', 'price', 'release_status', 'developer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['developer'].widget.attrs.update({'class': 'form-control'})
        self.fields['short_description'].widget.attrs.update({'class': 'form-control', 'cols': '50', 'rows': '2'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['release_status'].widget.attrs.update({'class': 'form-control'})