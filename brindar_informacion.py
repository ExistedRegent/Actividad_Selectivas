#Brindar informacion
consulta=input("Ingrese nombre de artista, pelicula o serie: ").lower()
match consulta:
    case "inception":
        info="Pelicula de ciencia ficcion dirigida por Christopher Nolan."
    case "the beatles":
        info="Banda de rock britanica formada en 1960."
    case "rick and morty":
        info="Serie animada de comedia y ciencia ficcion."
    case "stranger things":
        info="Serie de terror y ciencia ficcion de Netflix."
    case "avengers":
        info="Pelicula de superhéroes del MCU."
    case _:
        info="No se encontro informacion."
print("Informacion:", info)