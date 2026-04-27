from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import URL


def index(request):

    context = {
        'submitted': False,
        'duplicate_alias': False,
    }

    if request.method == 'POST':
        data = request.POST
        longurl = data.get('longurl', '').strip()
        custom_name = data.get('custom_name', '').strip()

        if custom_name and URL.objects.filter(custom_name=custom_name).exists():
            context['duplicate_alias'] = True
        else:
            obj = URL.objects.create(longurl=longurl, custom_name=custom_name)
            obj.save()

            context['submitted'] = True
            context['longurl'] = longurl
            context['custom_name'] = request.build_absolute_uri('/') + custom_name
            context['date'] = obj.date
            context['clicks'] = obj.clicks
    else:
        print("User is not sending anything")

    return render(request, 'index.html', context)
