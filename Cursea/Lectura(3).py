def calcular_edad(agno_nacimiento):
    agno_actual = 2017
    edad = agno_actual - agno_nacimiento - 1
    return edad

def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m) * 100)
    return estatura_m, estatura_cm

def actualizar_perfil():
    nombre = input("Para empezar, dime como te llamas. ")
    print()
    print("Hola ", nombre, ", bienvenido a Mi Red")
    print()

    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    edad = calcular_edad(agno)
    print()

    estatura_m, estatura_cm = obtener_estatura()

    num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

    print()
    print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("Amigos:  ", num_amigos)
    print("--------------------------------------------------")
    print()

nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = calcular_edad(agno)
print()

estatura_m, estatura_cm = obtener_estatura()

num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))

    if opcion == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")

    elif opcion == 2:
        mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
        print()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            print("--------------------------------------------------")
            print(nombre, "dice:", "@"+nombre_amigo, mensaje)
            print("--------------------------------------------------")

    elif opcion == 3:
        print("--------------------------------------------------")
        print("Nombre:   ", nombre)
        print("Edad:     ", edad, "años")
        print("Estatura: ", estatura_m, "m y ", estatura_cm, "centímetros")
        print("Amigos:   ", num_amigos)
        print("--------------------------------------------------")

    elif opcion == 4:
        actualizar_perfil()

    elif opcion == 0:
        print("Has decidido salir.")
    else:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")

print()
print("Gracias por usar Mi Red. ¡Hasta pronto!")
print()

#Si pruebas este cÃ³digo, verÃ¡s que funciona correctamente, pero nuestro programa ahora es bastante largo.
#Casi 140 lÃ­neas.
#Esto en sÃ­ no es malo. Sin embargo, si le pones atenciÃ³n, verÃ¡s que hay cÃ³digo que hemos tenido
#que repetir completamente. Por ejemplo, el cÃ³digo para mostrar el perfil de un usuario estÃ¡ escrito tres veces.
#Si ahora queremos agregar un nuevo dato del usuario, por ejemplo, el paÃ­s en que vive, debemos modificar
#al menos tres partes distintas del programa.
#Esto lo podemos hacer, talvez sin cometer errores, en un programa pequeÃ±o como Ã©ste.
#Pero en programas mÃ¡s grandes, es muy fÃ¡cil que nos olvidemos de actualizar una parte del cÃ³digo,
#o que no recordemos todas las partes que hay que modificar.

#Cuando tenemos instrucciones que se repiten tantas veces en distintas partes del programa,
# es una indicaciÃ³n de que talvez necesitamos agregar funciones.

#Te invitamos a pensar en al menos 3 alternativas o funcionalidades de este cÃ³digo
#que podrÃ­an convertirse en una funciÃ³n.