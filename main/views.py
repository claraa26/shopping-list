from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Clara Sista Widhiastuti',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# Create your views here.
