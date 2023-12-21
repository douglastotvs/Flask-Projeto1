#https://api.themoviedb.org/4/discover/movie?sort_by=popularity.desc&api_key=e1f0350b7743692640280055df5d89aa
#Filmes populares
import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=e1f0350b7743692640280055df5d89aa"

resposta = urllib.request.urlopen(url)

dados = resposta.read()

jsondata = json.loads(dados)

print(jsondata['results'])