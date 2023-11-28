from django import forms
from .models import Comments , Replay



class CommentForm(forms.ModelForm):


    class Meta:
        model = Comments
        fields = ['which_post', 'name', 'email', 'subject', 'message']


class ReplayForm(forms.ModelForm):


    class Meta:
        model = Replay
        fields = ['which_comment', 'message']