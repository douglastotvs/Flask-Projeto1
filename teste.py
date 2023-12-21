#api = https://api.themoviedb.org/4/discover/movie?sort_by=popularity.desc&api_key=e1f0350b7743692640280055df5d89aa
#img = http://image.tmdb.org/t/p/w500/hZkgoQYus5vegHoetLkCJzb17zJ.jpg
#Filmes populares
import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=e1f0350b7743692640280055df5d89aa"

resposta = urllib.request.urlopen(url)

dados = resposta.read()

jsondata = json.loads(dados)

print(jsondata['results'])

# import requests

# url = "https://api.themoviedb.org/3/account/20848123"

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMWYwMzUwYjc3NDM2OTI2NDAyODAwNTVkZjVkODlhYSIsInN1YiI6IjY1ODQxYWI4Y2E4MzU0NDEwM2Q3YTU3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Nlud_nfGLq5upqGaS661u4oQ4xk1UCysPCRJ4eWEuPQ"
# }

# response = requests.get(url, headers=headers)

# print(response.text)