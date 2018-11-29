from django import forms
import datetime

from .models import PROFILE
from .models import QUESTIONS
from django.contrib.auth.models import User



class registerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["email","first_name","last_name","password","username"]


        #model = ACCOUNTS
        #fields=['email','name','surname','username','password','birthday','gender','language']
        
    def __init__(self, *args, **kwargs):
        super(registerForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class":"form-control","placeholder":"E mail"})
        self.fields["first_name"].widget.attrs.update({"class":"form-control","placeholder":"Name"})
        self.fields["last_name"].widget.attrs.update({"class":"form-control","placeholder":"Surname"})
        self.fields["username"].widget.attrs.update({"class":"form-control","placeholder":"Username"})
        self.fields["password"].widget.attrs.update({"class":"form-control","placeholder":"Password"})
        
    

    def clean_username(self):
        data = self.cleaned_data["username"]

        if len(data) > 20:
            raise forms.ValidationError("KUllanıcı adı 20 karakterden fazla")  
        return data

class profileForm(forms.ModelForm):

    birthday = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(1975, 2000)))
    class Meta:
        model = PROFILE
        fields = ["birthday","gender","language"]
    def __init__(self, *args, **kwargs):
        super(profileForm,self).__init__(*args,*kwargs)
        self.fields["birthday"].widget.attrs.update({"class":"form-control","placeholder":"Birthday","type":"date"})
        self.fields["gender"].widget.attrs.update({"class":"form-control","placeholder":"Gender"})
        self.fields["language"].widget.attrs.update({"class":"form-control","placeholder":"Language"})
        

class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    


class askForm(forms.ModelForm):
    question = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = QUESTIONS
        fields = ["question","answer_one","answer_two","answer_three","answer_true"]
    def __init__(self, *args, **kwargs):
        super(askForm,self).__init__(*args,*kwargs)
        self.fields["question"].widget.attrs.update({"class":"form-control","placeholder":"Soru Sor","cols":"80","rows":"3","onkeyup":"countChar(this)","id":"field"})
        self.fields["answer_one"].widget.attrs.update({"class":"form-control","placeholder":"İlk Cevap"})
        self.fields["answer_two"].widget.attrs.update({"class":"form-control","placeholder":"İkinci Cevap"})
        self.fields["answer_three"].widget.attrs.update({"class":"form-control","placeholder":"Üçüncü Cevap"})
        self.fields["answer_true"].widget.attrs.update({"class":"form-control form-control-success","placeholder":"Doğru Cevap"})
        
        
