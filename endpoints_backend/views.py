from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

# Create your views here.

def users(request):
  response=requests.get('https://jsonplaceholder.typicode.com/users')

  users=response.json()
  return JsonResponse(users, safe=False)

@csrf_exempt
def pokemonByName(request):
  if request.method=='POST':
    url='https://pokeapi.co/api/v2/pokemon/{}'.format(json.loads(request.body)['name'])
    
    response=requests.get(url)

    pokemon=response.json()
    return JsonResponse(pokemon, safe=False)

  return JsonResponse({'error':True})

def pokemonId(request, id):
  url = 'https://pokeapi.co/api/v2/pokemon-form/{}'.format(id)

  response=requests.get(url)
  pokemon=response.json()
  return JsonResponse(pokemon, safe=False)

@csrf_exempt
def characterList(request):
  if request.method=='POST':
    url='https://rickandmortyapi.com/api/character?page={}'.format(json.loads(request.body)['page'])
    print(url, request.body)
    response=requests.get(url)

    pokemon=response.json()
    return JsonResponse(pokemon, safe=False)

  return JsonResponse({'error':True})

def locationById(request, id):
  url = 'https://rickandmortyapi.com/api/location/{}'.format(id)

  response=requests.get(url)
  pokemon=response.json()
  return JsonResponse(pokemon, safe=False)