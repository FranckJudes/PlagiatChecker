from django import forms
from plagiatLocal.models import DocumentForm

class DocumentForm(forms.ModelForm): 
    class Meta:
        model = DocumentForm
        fields = "__all__"
        

