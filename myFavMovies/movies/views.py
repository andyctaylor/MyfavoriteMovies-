from django.shortcuts import render


# Create your views here.
def index(request):
    # Here's where we store the contacts variable
    context = {"movies": ["The One", "Hercules", "A Goofy Movie", "The matrix"]}

    # Render takes in a request, app name/file name, Then a dictionary (Context) if needed.
    return render(request, "movies/index.html", context)


# Create your views here.
def about(request):
    return render(request, "movies/about-me.html", {})
