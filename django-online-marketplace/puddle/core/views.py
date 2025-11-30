from django.shortcuts import render  # type: ignore[import]

def index(request):
    return render(request, 'core/index.html') 
# Renders the homepage template located at core/index.html