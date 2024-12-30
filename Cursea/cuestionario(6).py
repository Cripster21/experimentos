def funcion_misteriosa(x):
  for i in range(2,x):
    if x % i == 0:
      return False
  return True

print("La funcion misteriosa con x = 102 devuelve:",funcion_misteriosa(102))
print("La funcion misteriosa con x = 103 devuelve:",funcion_misteriosa(103))


from random import randint
a = randint(1,10)

print(a)


def funcion_misteriosa(x):
  c=0
  while x!=0:
    c+=1
    x = x//10
  return c

print(funcion_misteriosa(10000))


def suma(N):
  s=0
  for i in range(N):
    s+=i
  return s+N

print(suma(5))

def f(x,y):
  print("Funcion f")
  return x**2+y**2
  print("Final de la función")

print(f(2,3))

def funcion(x,y):
  return (x-8)*(y**2)

funcion(16,1)