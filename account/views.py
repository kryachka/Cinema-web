from django.shortcuts import render

from account.forms import ProfileForm
from products.models import *
# Create your views here.
def account(request):
    name = "Congrat"
    form = ProfileForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data=form.cleaned_data
        print(data['name'])

        new_form=form.save(

        )
    return render(request, 'base/base.html', locals())
def home(request):
    products_images=ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'base/home.html', locals())
