lat = -33.499188
lon = -70.615126

lat_domicilio = float(input("Ingresa la latitud de tu domicilio"))
lon_domicilio = float(input("Ingresa la longitud de tu domicilio"))
estoy_al_sur = lat_domicilio - lat > 0

print("Estoy al sur:", float(estoy_al_sur))
print("Estoy al sur:", estoy_al_sur)