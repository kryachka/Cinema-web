from django.shortcuts import render



def account(request):
    return render(request, 'base/base.html', locals())
