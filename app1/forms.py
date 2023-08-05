from django import forms
from app1.models import *
  


class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'




class WebpageModelForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'  
        widgets={'topic_name':forms.RadioSelect,'name':forms.Textarea()}
              