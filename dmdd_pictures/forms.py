from django import forms
from dmdd_pictures.models import PictureInfo

class LogForm(forms.ModelForm):
    class Meta:
        model = PictureInfo
        fields = ('gene', 'identifier', 'slide', 'imgsrc', 'mutated', 'comment', 'submission', 'author', 'wildtype', 'center', 'leftPresent',
        'leftBeginning', 'rightPresent', 'rightBeginning',)