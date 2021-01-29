from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request, 'myapp1/myone.html', {'title':'My Django Web', 'cname':'my site'})