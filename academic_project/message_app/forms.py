from django import forms
from .models import Message, Comment


# Yassine Ibhir
# This class creates a form for a message
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['message'].label = ""
        self.fields['message'].widget = forms.TextInput(attrs={'placeholder': "Write your message.."})


# Yassine Ibhir
# This class creates a form for The comments
class CommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'placeholder': 'Write a comment',
            'rows': 4,
            'cols': 30
        }
    ))

    class Meta:
        model = Comment
        fields = ['comment']
