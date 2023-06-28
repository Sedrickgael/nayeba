from django.shortcuts import render


# Create your views here.
def contact(request):
    datas = {

    }
    return render(request, 'contact-us.html', datas)