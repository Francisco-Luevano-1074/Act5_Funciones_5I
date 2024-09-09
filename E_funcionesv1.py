print("Manejo de funciones V1")
def Hola_mundo():
    print("Hola, aquí estoy, dentro de la función.")
    
def Mensa(msg):
    print(msg)    
def EscribeNC(Nombre,Apellido):
    print(Nombre, Apellido)
    print(f"Tu nombre completo es {Nombre} {Apellido}")
def suma2numeros(n1,n2):
    s=n1+n2
    return f"La suma de {n1} y de {n2} es de:",s
# Llamando a la función
Hola_mundo()
Mensa("Hola, what's up?") # Llama a la funció Mensa con un parámetro
Mensa("El profe me sorprendió enviando mensajes") # Llama a la función con un parámetro
EscribeNC("Francisco", "Luévano")
print("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))