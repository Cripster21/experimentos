import S5Red as Red
import os

def limpiar_nombre_archivo(nombre):
    # Eliminar caracteres no imprimibles al final y al inicio del nombre del archivo
    return nombre.strip()

def leer_datos_usuario(nombre_archivo):
    # Lee los datos del usuario desde un archivo y los retorna como una tupla
    with open(nombre_archivo, "r") as archivo_usuario:
        nombre = archivo_usuario.readline().strip()
        edad = int(archivo_usuario.readline())
        estatura = float(archivo_usuario.readline())
        estatura_m = int(estatura)
        estatura_cm = int((estatura - estatura_m) * 100)
        sexo = archivo_usuario.readline().strip()
        pais = archivo_usuario.readline().strip()
        num_amigos = int(archivo_usuario.readline())
        estado = archivo_usuario.readline().strip()
    
    return nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado

def escribir_datos_usuario(nombre_archivo, datos_usuario):
    # Escribe los datos del usuario en un archivo
    nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado = datos_usuario
    with open(nombre_archivo, "w") as archivo_usuario:
        archivo_usuario.write(nombre + "\n")
        archivo_usuario.write(str(edad) + "\n")
        archivo_usuario.write(str(estatura_m + estatura_cm / 100) + "\n")
        archivo_usuario.write(sexo + "\n")
        archivo_usuario.write(pais + "\n")
        archivo_usuario.write(str(num_amigos) + "\n")
        archivo_usuario.write(estado + "\n")

def cambiar_usuario():
    nuevo_nombre = input("Ingrese el nombre de usuario al que desea cambiar: ")
    if Red.existe_archivo(nuevo_nombre + ".user"):
        return Red.leer_usuario(nuevo_nombre)
    else:
        print("No se pudo encontrar un usuario con ese nombre.")
        return None

# Mostramos la bienvenida y obtenemos el nombre del usuario
Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

# Verificamos si el archivo existe y limpiamos el nombre del archivo
nombre_archivo = limpiar_nombre_archivo(nombre + ".user")
if os.path.isfile(nombre_archivo):
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    datos_usuario = leer_datos_usuario(nombre_archivo)
else:
    print()
    edad = Red.obtener_edad()
    estatura_m, estatura_cm = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    num_amigos = Red.obtener_num_amigos()
    estado = ""
    datos_usuario = (nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado)

# En ambos casos, al llegar aquí ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(*datos_usuario[:7])
Red.mostrar_mensaje(*datos_usuario[:2], datos_usuario[7])

# Ahora podemos mostrar el menú y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, None, estado)
    elif opcion == 2:
        estado = Red.obtener_mensaje()
        for _ in range(datos_usuario[6]):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.mostrar_mensaje(nombre, nombre_amigo, estado)
    elif opcion == 3:
        Red.mostrar_perfil(*datos_usuario[:7])
    elif opcion == 4:
        edad = Red.obtener_edad()
        estatura_m, estatura_cm = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        num_amigos = Red.obtener_num_amigos()
        datos_usuario = (nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado)
        Red.mostrar_perfil(*datos_usuario[:7])
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ", nombre_archivo)
        escribir_datos_usuario(nombre_archivo, datos_usuario)
        print("Archivo", nombre_archivo, "guardado")

print("Gracias por usar Mi Red. ¡Hasta pronto!")
