from flask import Flask, render_template, request, redirect, url_for
import urllib.request, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.sqlite3"

db = SQLAlchemy(app)
app.app_context().push()

frutas = []
registros=[]

class cursos(db.Model):
	id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(50))
	descricao = db.Column(db.String(100))
	ch = db.Column(db.Integer)
	
	def __init__(self, nome, descricao, ch):
		self.nome = nome
		self.descricao = descricao
		self.ch = ch

@app.route('/', methods=["GET", "POST"])
def principal():
	#frutas = ["Morango", "Uva", "Laranja", "Mamão", "Maçã", "Pêra", "Melão", "Abacaxi"]
	if request.method == "POST":
		if request.form.get("fruta"):
			frutas.append(request.form.get("fruta"))
	return render_template("index.html", frutas=frutas)


@app.route('/sobre', methods=["GET", "POST"])
def sobre():
	#notas = {"Fulano":5.0, "Beltrano":6.0, "Aluno": 7.0, "Sicrano":8.5, "Rodrigo":9.5}
	if request.method == "POST":
		if request.form.get("aluno") and request.form.get("nota"):
			registros.append({"aluno": request.form.get("aluno"),"nota": request.form.get("nota")})

	return render_template("sobre.html", registros=registros)

@app.route('/filmes/<propriedade>')
def filmes(propriedade):
	if propriedade == 'populares':
		url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=e1f0350b7743692640280055df5d89aa"
	elif propriedade == "kids":
		url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=e1f0350b7743692640280055df5d89aa"
	elif propriedade == "2010":
		url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=e1f0350b7743692640280055df5d89aa"
	elif propriedade == "drama":
		url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=e1f0350b7743692640280055df5d89aa"	
	elif propriedade == "tom_cruize":
		url="https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=e1f0350b7743692640280055df5d89aa"

	resposta = urllib.request.urlopen(url)
	dados = resposta.read()
	jsondata = json.loads(dados)

	return render_template("filmes.html", filmes=jsondata['results'])

@app.route('/cursos')
def lista_cursos():
	return render_template("cursos.html", cursos=cursos.query.all())

@app.route('/cria_curso', methods=['GET', "POST"])
def cria_curso():
	nome = request.form.get('nome')
	descricao = request.form.get('descricao')
	ch = request.form.get('ch')

	if request.method == 'POST':
		curso = cursos(nome, descricao, ch)
		db.session.add(curso)
		db.session.commit()
		return redirect(url_for('lista_cursos'))

	return render_template("novo_curso.html")

if __name__ =="__main__":	
	db.create_all()
	app.run(debug=True)
	