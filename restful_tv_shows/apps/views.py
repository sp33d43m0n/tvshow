from django.shortcuts import render, HttpResponse, redirect
from apps.models import Show
from datetime import *
from time import gmtime, strftime
from .models import Show, ShowManager
from django.contrib import messages

# Create your views here.
# *********************************************
# 1. # GET /shows/new ------ 'show' was 'shows'
def AddNewShow(request): # GET /shows/new
        # show= Show.objects.all()
        # context = {'id': show.id,'show': show.title, 'network': show.network, 'release_date': show.release_date, 'description': show.description}
        return render(request, 'AddNewShow.html')
# *********************************************
#2. # POST /shows/create
def CreateNewShow(request): # POST /shows/create
    print(request.POST)

    title=request.POST['title']
    network=request.POST['network']
    release_date=request.POST['release_date']
    #release_date=release_date.strftime('%Y-%m-%d')
    description=request.POST['description']

    print('*'*10,release_date)


    errors= Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for valor in errors.values():
            messages.error(request, valor)
        return render(request, 'AddNewShow.html')
    else:
        newSHow=Show.objects.create(title=title, network=network, release_date=release_date, description=description)
        messages.success(request, "Usuario agregado con exito!!")
        show_url=f'/shows/{newSHow.id}'
        print(show_url)
        return redirect(show_url)


# *********************************************
# 3. GET shows/id
def TvShow(request, id): # GET /shows/<id>
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'TVShow.html', context)
# *********************************************
# 4 GET /shows ------ 'show' was 'shows'
def AllShows(request): # GET /shows
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'AllShows.html', context)
# *********************************************
# 5 GET /shows/<id>
def EditShow(request, id):

    show = Show.objects.get(id=id)
    context = {'id': show.id, 'show': show.title, 'network': show.network, 'release_date': show.release_date, 'description': show.description}
    return render(request, 'EditShow.html', context)
# *********************************************
# 6 POST shows/<id>/update
def UpdateShow(request, id):
    show = Show.objects.get(id=id)
    print(request.POST)


    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    fecha= request.POST['release_date']
    print(fecha)
    fecha=fecha.strptime('%Y-%m-%d')
    # show.release_date = show.release_date.strftime('%Y-%m-%d')
    show.description = request.POST['description']


    context = {'id': show.id, 'show': show.title, 'network': show.network, 'release_date': fecha, 'description': show.description}
    print(context)
    # show.save()
    # return redirect(f'/shows/{id}')
    errors= Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for valor in errors.values():
            messages.error(request, valor)
        # return render(request, 'EditShow.html')
        # return redirect(f'/shows/{id}/edit')
        return render(request, 'EditShow.html', context)
    else:
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        # show.release_date = show.release_date.strftime('%Y-%m-%d')
        show.description = request.POST['description']
        show.save()

        # print(show.title)
        messages.success(request, "Usuario agregado con exito!!")
        return redirect(f'/shows/{id}')
# *********************************************
# 7 POST shows/<id>/destroy
def DeleteShow(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')
# *********************************************
# 8 POST /shows Root Rout redirects to /shows
def index(request):
    return redirect('/shows')