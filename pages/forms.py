from django import forms
from .models import *

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "h-full-width h-remove-bottom"
        self.fields["email"].widget.attrs["class"] = "h-full-width h-remove-bottom"
        self.fields["message"].widget.attrs["class"] = "h-full-width"
        self.fields["name"].widget.attrs["placeholder"] = "Your Name"
        self.fields["email"].widget.attrs["placeholder"] = "Your Email"
        self.fields["message"].widget.attrs["placeholder"] = "Your Message"