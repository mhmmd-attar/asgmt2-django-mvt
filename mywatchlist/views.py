from django.shortcuts import render, redirect
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def redirect_to_html(request):
    return redirect('/mywatchlist/html/')

def show_mywatchlist(request):
    data_mywatchlist_item = MyWatchList.objects.all()
    watched = 0
    for item in data_mywatchlist_item:
            watched += 1 if item.watched == 'Y' else -1
    message = "Congratulations, you have watched a lot of movies" if watched >=0 else "Woah, you need to watch more movies"
    context = {
        'list_item': data_mywatchlist_item,
        'name': 'Mohammad Attar',
        'npm': '2106657992',
        'message': message,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(request):
    data =MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")