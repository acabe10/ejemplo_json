import json
with open("movies.json") as fichero:
	doc=json.load(fichero)

def listar(doc):
	peliculas=[]
	year=[]
	duracion=[]
	for info in doc:
		peliculas.append(info["title"])
		year.append(info["year"])
		duracion.append(info["duration"])
	return zip(peliculas,year,duracion)

def pelis_actores(doc):
	titulos=[]
	actores=[]
	for i in doc:
		titulos.append(i["title"])
		actores.append(i["actors"])
	return zip(titulos,actores)

def palabras_dadas(doc,palabras):
	pelis=[]
	for i in doc:
		if palabras[0] and palabras[1] in i["storyline"]:
			pelis.append(i["title"])
	return pelis

def comprobador(doc,palabras):
	for i in doc:
		if palabras[0] and palabras[1] in i["storyline"]:
			return True
		else:
			return False

def actor_pelis(doc,actor):
	pelis=[]
	for i in doc:
		if actor in i["actors"]:
			pelis.append(i["title"])
	return pelis

while True:
	print()
	print("1.Listar el título, año y duración de todas las películas.")
	print("2.Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una.")
	print("3.Mostrar las películas que contengan en la sinopsis dos palabras dadas.")
	print("4.Mostrar las películas en las que ha trabajado un actor dado.")
	print("5.Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.")
	print("0.Salir")
	print()
	opcion=int(input("Elige opción: "))
	print()

	if opcion == 0:
		print()
		print("Adiós!")
		print()
		break;

	elif opcion == 1:
		for titulo,year,duracion in listar(doc):
			print("Título: ",titulo)
			print("Año: ",year)
			print("Duración: ",duracion.strip("PT").strip("M"),"minutos")
			print("_"*50)

	elif opcion == 2:
		for titulo,actores in pelis_actores(doc):
			print("Título: ",titulo)
			print("Actores:")
			for i in actores:
				print(i)
			print("_"*50)

	elif opcion == 3:
		palabras=[]
		for i in range(2):
			palabra = input("Palabra %i: "% (i+1))
			palabras.append(palabra)
		comprobacion=comprobador(doc,palabras)
		if comprobacion == True:
			print("Las palabras %s y %s están en la sipnosis de las siguientes películas:" % (palabras[0],palabras[1]))
			print()
			for pelis in palabras_dadas(doc,palabras):
				print(pelis)
				print("_"*50)
		else:
			print()
			print("No hay palabras que coincidan.")

	elif opcion == 4:
		actor=input("Dime un actor")
		print("El actor %s ha trabajado en las siguientes películas"%actor)
		for pelis in actor_pelis(doc,actor):
			print(pelis)
			print("_"*50)

	else:
		print()
		print("Error de opción")
		print()