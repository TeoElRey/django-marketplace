from django import forms
from .models import Item

INPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ('category', 'name', 'description', 'price', 'image')
    widgets = {
    'category': forms.Select(attrs= {
       'class': INPUT_CLASS
    }),
    'name': forms.TextInput(attrs= {
       'class': INPUT_CLASS,
       'placeholder': "Your name"
    }),
    'description': forms.Textarea(attrs= {
       'class': INPUT_CLASS,
       'placeholder': "Describe your product"
    }),
    'price': forms.TextInput(attrs= {
       'class': INPUT_CLASS,
       'placeholder': "Please do not use any commas to separate large values"
    }),
    'image': forms.FileInput(attrs= {
       'class': INPUT_CLASS
    }),
  }
    
class EditItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ('name', 'description', 'price', 'image', 'is_sold')
    widgets = {
    'name': forms.TextInput(attrs= {
       'class': INPUT_CLASS,
       'placeholder': "Your name"
    }),
    'description': forms.Textarea(attrs= {
       'class': INPUT_CLASS,
       'placeholder': "Describe your product"
    }),
    'price': forms.TextInput(attrs= {
       'class': INPUT_CLASS,
       'placeholder': "Please do not use any commas to separate large values"
    }),
    'image': forms.FileInput(attrs= {
       'class': INPUT_CLASS
    }),
  }