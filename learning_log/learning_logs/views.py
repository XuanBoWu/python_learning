from django.shortcuts import render

# Create your views here.
def index(request):
    """ index of learning logs """

    return render(request, 'learning_logs/index.html')
