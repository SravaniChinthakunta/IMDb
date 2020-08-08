from django.shortcuts import render
from app1.middleware import fetchdata
from IMDB.settings import IMDB_FILE
from django.http import HttpResponse
from django.contrib.messages import error
import json

def dict_data():

    dict_data = json.loads(open(IMDB_FILE).read())
    titles = [x['title'][0:len(x['title']) - 1] for x in dict_data if
              x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                  'plot'] != '']
    posters = [x['poster'] for x in dict_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    trailer_links = [x['trailer']['link'] for x in dict_data if
                     x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                         'plot'] != '']
    ratings = [x['rating'] for x in dict_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    plots = [x['plot'] for x in dict_data if
             x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                 'plot'] != '']

    # print(titles)
    # print(len(ratings))
    # print(len(posters))

    context = [{'title': title, 'poster': poster, 'rating': rating, 'plot': plot, 'trailer': trailer} for
               title, poster, rating, plot, trailer in zip(titles, posters, ratings, plots, trailer_links)]
    return context

#==================================================================================


def showindex(request):
#1 first change ikkada aa name iccha data kosam dit variable assigniing
    dict = dict_data()
    print(dict)
    return render(request,"index.html",{'data':dict})

def moviename(request):
    name=request.GET.get("name")
    dict = dict_data()
    print(dict)
    for x in dict:
        if x['title']==name:
            print(x)
            return render(request,"browserdata.html",{'moviedetails':x})
        else:
            error(request,'Movie Notfound ')
            return HttpResponse('Enter movie name correctly')
# Create your views here.
