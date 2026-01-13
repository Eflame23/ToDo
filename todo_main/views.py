from django.shortcuts import render

# def home(request):
#     return render(request,'home.html')


from datetime import date

def home(request):
    return render(request, "home.html", {
        "today": date.today()
    })
