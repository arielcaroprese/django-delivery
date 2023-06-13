from django import forms

class ProductForm(forms.Form):
    title = forms.CharField()
    price = forms.IntegerField()

class CategoryForm(forms.Form):
    title = forms.CharField()
    price = forms.IntegerField()

class CouponForm(forms.Form):
    title = forms.CharField()
    price = forms.IntegerField()

class ProductSearch(forms.Form):
    title = forms.CharField()