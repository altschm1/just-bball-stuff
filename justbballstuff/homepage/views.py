from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'homepage/home.html', {'title_head': 'Just BBall Stuff', 'home':True})

def about(request):
    return render(request, 'homepage/about.html', {'title_head': 'Just BBall Stuff: About', 'about':True})
