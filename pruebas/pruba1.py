# Solicitar nombre de usuario y contraseña
password = input('Password: ')
errors = []

# Verificar validación de caracteres
if len(password) < 8:
    errors += ['Debe tener al menos 8 caracteres']
if not any(char.islower() for char in password):
    errors += ['Debe tener al menos una minúscula [a-z]']
if not any(char.isupper() for char in password):
    errors += ['Debe tener al menos una mayúscula [A-Z]']
if not any(char.isalpha() for char in password):
    errors += ['Debe tener al menos una letra [a-z]']
if not any(char.isdigit() for char in password):
    errors += ['Debe tener al menos un dígito [0-9]']
if not any(char == ',' for char in password):
    errors += ['Debe tener al menos una coma [ , ]']
if not any(char == ';' for char in password):
    errors += ['Debe tener al menos un punto y coma [ ; ]']

# Mostrar errores o confirmar éxito
if errors:
    for error in errors:
        print(error)
else:
    print('Su password cumple con todas las reglas')
