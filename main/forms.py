from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name','id':'nam'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email','id':'email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5,'id':'mass'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''