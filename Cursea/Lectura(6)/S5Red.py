
def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
    return 2017-agno-1

def obtener_estatura():
    estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return (metros, centimetros)

def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    return sexo

def obtener_pais():
    pais = input("Indica tu paÃ­s de nacimiento: ")
    return pais

def obtener_num_amigos():
    amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))
    return amigos

def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    na = obtener_num_amigos()
    return (n,e,em,ec,na)

def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos):
    print("--------------------------------------------------")
    print(f"Nombre:    {nombre}")
    print(f"Edad:      {edad} años")
    print(f"Estatura:  {estatura_m} m y {estatura_cm} cm")
    print(f"Sexo:      {sexo}")
    print(f"País:      {pais}")
    print(f"Amigos:    {num_amigos}")
    print("--------------------------------------------------")


def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  5. Cambiar de usuario")  # Nueva opción
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 5:  # Ajusta el rango para incluir la nueva opción
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion


def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. Â¿QuÃ© piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")
