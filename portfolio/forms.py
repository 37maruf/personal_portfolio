from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    # Hidden trap field. Real visitors never see it, so bots that fill it get blocked.
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "tabindex": "-1", "autocomplete": "off", "aria-hidden": "true",
    }))

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com", "autocomplete": "email"}),
            "subject": forms.TextInput(attrs={"placeholder": "What is this about?"}),
            "message": forms.Textarea(attrs={"placeholder": "Write your message here", "rows": 6}),
        }

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Spam detected.")
        return ""

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 10:
            raise forms.ValidationError("Please write at least 10 characters.")
        return message
