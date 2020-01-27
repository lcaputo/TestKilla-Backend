from django.http import HttpResponse
import requests
import json
from .themoviedb import token

headers = {'Authorization': 'Bearer '+token}


def movies(request):
    if request.method == 'GET':
        bestMovies = requests.get('https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc',
                                  headers=headers).json()
        response = []
        for movie in bestMovies['results']:
            movieID = movie['id']
            movieDet = requests.get(
                "https://api.themoviedb.org/3/movie/" + str(movieID), headers=headers).json()
            if len(movieDet['production_companies']) > 0:
                movieDet['production_companies'] = movieDet['production_companies'][0]['name']
            if len(movieDet['genres']) > 0:
                txt = ''
                for i in range(len(movieDet['genres'])):
                    txt = txt + movieDet['genres'][i]['name']
                    if not i == len(movieDet['genres']) - 1:
                        txt += ' | '
            Obj = {
                'id': movie['id'],
                'title': movie['title'],
                'production_company': movieDet['production_companies'],
                'vote_average': movie['vote_average'],
                'genres': txt,
                'overview': movie['overview'],
                'release_date': movie['release_date'],
                'original_language': movie['original_language'],
                'popularity': movie['popularity'],
                'cover_image': movie['poster_path'],
                'backdrop_image': movie['backdrop_path'],
                'video': movie['video'],
                'adult': movie['adult']
            }
            response.append(Obj)
            response = response[:10]
        return HttpResponse(json.dumps(response, indent=4), content_type="application/json", status=200)
    return HttpResponse(json.dumps({'error': 'metodo incorrecto'}, indent=4), content_type="application/json", status=405)


def movieById(request, id):
    if request.method == 'GET':
        movieDet = requests.get(
            "https://api.themoviedb.org/3/movie/" + str(id), headers=headers).json()
        if len(movieDet['production_companies']) > 0:
            movieDet['production_companies'] = movieDet['production_companies'][0]['name']
        if len(movieDet['genres']) > 0:
            txt = ''
            for i in range(len(movieDet['genres'])):
                txt = txt + movieDet['genres'][i]['name']
                if not i == len(movieDet['genres']) - 1:
                    txt += ' | '
        movieData = {
            'id': movieDet['id'],
            'title': movieDet['title'],
            'production_company': movieDet['production_companies'],
            'vote_average': movieDet['vote_average'],
            'vote_count': movieDet['vote_count'],
            'genres': txt,
            'overview': movieDet['overview'],
            'release_date': movieDet['release_date'],
            'original_language': movieDet['original_language'],
            'popularity': movieDet['popularity'],
            'cover_image': movieDet['poster_path'],
            'backdrop_image': movieDet['backdrop_path'],
            'video': movieDet['video'],
            'adult': movieDet['adult'],
        }
        response = []
        response.append(movieData)
        return HttpResponse(json.dumps(response, indent=4), content_type="application/json", status=200)
    return HttpResponse(json.dumps({'error': 'metodo incorrecto'}, indent=4), content_type="application/json", status=405)


def movieCast(request, id):
    if request.method == 'GET':
        movieCredits = requests.get(
            "https://api.themoviedb.org/3/movie/" + str(id) + "/credits", headers=headers).json()
        movieCast = []
        for cast in movieCredits['cast']:
            Obj = {
                'character': cast['character'],
                'name': cast['name'],
                'picture': cast['profile_path'],
            }
            movieCast.append(Obj)
        return HttpResponse(json.dumps(movieCast, indent=4), content_type="application/json", status=200)
    return HttpResponse(json.dumps({'error': 'metodo incorrecto'}, indent=4), content_type="application/json", status=405)

