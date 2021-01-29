from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request, 'myapp2/my11.html', {'title':'My Django Web', 'cname':'my favorite site'})