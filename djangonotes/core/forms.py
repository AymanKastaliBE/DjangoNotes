from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control text-bg-secondary border-0', 'rows': '3'}))
    
    class Meta:
        model = Note
        fields = ['content']