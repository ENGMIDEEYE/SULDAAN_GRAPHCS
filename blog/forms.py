from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Category, Post ,Visitors ,Management

class Category_Model_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['Name']

class Post_Model_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title','Category','Image','Desc','Publish','Tags']

class Management_Model_form(forms.ModelForm):
    class Meta:
        model = Management
        fields = ['Name','Desc','Image','Email','Facebook','Twitter','Whatsapp']

class Visitors_Model_form(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = ['Name','Desc']