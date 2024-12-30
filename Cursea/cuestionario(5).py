def sueldo(cargo):
  dinero = 0
  # aquí debes implementar tu código
  # modificando la variable dinero
  if cargo == "Ejecutivo":
    dinero = 90
    print("El Ejecutivo tiene $",dinero)
  elif cargo == "Jefe":
    dinero = 100
    print("El Jefe tiene $",dinero)
  elif cargo == "Externo":
    dinero = 50
    print("El Externo tiene $",dinero)
  else:
    print("El cargo no existe")
  # (no modifiques nada de las lineas anteriores)
  return dinero

def exponenciacion(numero):
  resultado = numero
  # aquí debes implementar tu código
  # modificando la variable resultado
  if numero % 2 == 0:
    resultado **= 3
  else:
    resultado **= 2
  # (no modifiques nada de las lineas anteriores)
  return resultado

def es_primo(numero):
  primo = True
  # aquí debes implementar tu código
  # modificando la variable primo 
  if numero <= 1:
    primo = False
  else:
    for i in range(2,numero):
     if numero % i == 0:
        primo = False
        break
  # (no modifiques nada de las lineas anteriores)
  return primo
