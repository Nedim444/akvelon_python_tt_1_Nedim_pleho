from django import forms
from .models import User, Transaction
# create class Form which will help to implement function in view
# Fields  contain all fields  which will be use from models.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('amount','date')