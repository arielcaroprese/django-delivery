from django import forms

class ProductForm(forms.Form):
    title = forms.CharField()
    price = forms.IntegerField()
    category_id = forms.IntegerField()

class CategoryForm(forms.Form):
    title = forms.CharField()

class CouponForm(forms.Form):
    coupon = forms.CharField()
    discount = forms.IntegerField()

class ProductSearch(forms.Form):
    title = forms.CharField()