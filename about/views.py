from django.shortcuts import render


# Create your views here.
def about(request):
    datas = {

    }
    return render(request, 'about-us.html', datas)