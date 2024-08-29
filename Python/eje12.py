calificacion = int(input("Introduce una calificación (0-10): "))

if 0 <= calificacion <= 2:
    print("Muy Malo")
elif 3 <= calificacion <= 4:
    print("Malo")
elif 5 <= calificacion <= 6:
    print("Regular")
elif 7 <= calificacion <= 8:
    print("Muy Bueno")
elif 9 <= calificacion <= 10:
    print("Excelente")
else:
    print("Calificación fuera de rango. Debe ser entre 0 y 10.")
