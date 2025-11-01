from django.shortcuts import render

def filter(request):
    return render(request, template_name='opencv/filter.html')