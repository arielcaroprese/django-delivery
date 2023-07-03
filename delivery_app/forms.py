from django import forms
from .models import Categories, Reviews

class ProductForm(forms.Form):
    title = forms.CharField()
    price = forms.IntegerField()
    category_id = forms.ModelChoiceField(queryset=Categories.objects.all(), to_field_name="id", empty_label=None)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    image = forms.ImageField(label='Imagen')

class CategoryForm(forms.Form):
    title = forms.CharField()
    image = forms.ImageField(label='Imagen')

class ProductSearch(forms.Form):
    title = forms.CharField()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude = ['product', 'author', 'created_at']
    """  title = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    star_rating = forms.IntegerField(min_value=1, max_value=5) """

