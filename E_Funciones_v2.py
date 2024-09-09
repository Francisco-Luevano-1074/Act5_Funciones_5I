print("Funciones creadas por el usuario")
# Las funciones
def Mi_lista():
    print("--Amigos de el profe Nava--")
    amigos=["Homero","Paty","Lety"]
    for nava in amigos:
        print(nava)
def Mi_tupla():
    print("--Deportes--")
    deportes=("Fútbol","Beis","Basket")
    for gimnasio in deportes:
        print(gimnasio)
def Mi_dic():
    print("--Sneakers--")
    Sneakers = {
        "Marca":"Adidas",
        "Modelo":"Forum Mod Low",
        "Color":"Azul",
        "Talla":6
    }
    for unidad in Sneakers:
        print(unidad)
def Mi_conjunto():
    print("--Ropa--")
    ropa = ("Gorra","Cadena","Camiseta","Pantalón","Sneakers")
    for fit in ropa:
        print(fit)
# Llamando a la funciones
Mi_lista()
Mi_tupla()
Mi_dic()
Mi_conjunto()
