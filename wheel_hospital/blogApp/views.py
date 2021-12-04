from django.shortcuts import render
from .models import blogModel

# Create your views here.
def blogView(request):
    allblogs = blogModel.objects.all().order_by('-id')
    context = {
        'allblogs': allblogs
    }
    return render(request, 'blog.html', context)
