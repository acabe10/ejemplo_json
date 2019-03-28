import json
with open("movies.json") as fichero:
	doc=json.load(fichero)

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

#	elif opcion == 1:
		
	    
	else:
		print()
		print("Error de opción")
		print()