# Datos iniciales


otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_med = 4
curso_de_dalto = 1.5

# Calculando diferencias de tiempo en porcentaje
dif_min = 100 - curso_de_dalto / otros_cursos_min * 100
dif_media = 100 - curso_de_dalto / otros_cursos_med * 100
dif_max = round(100 - curso_de_dalto / otros_cursos_max * 100, 1)


# Mensajes de diferencias de tiempo
print(
    f"La diferencia con el curso de menor duración en porcentajes es de {dif_min}% más rápido"
)
print(
    f"La diferencia con el curso de duración media en porcentajes es de {dif_media}% más rápido"
)
print(
    f"La diferencia con el curso de mayor duración en porcentajes es de {dif_max}% más rápido"
)

print("----------------------------")
print("CRUDOS:")

# Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5
# Calculando diferencias de crudos
dif_final_crudo_otros_cursos = round(100 - otros_cursos_med / crudo_promedio * 100, 1)
dif_final_crudo_dalto = round(100 - curso_de_dalto / crudo_dalto * 100, 1)

# Mensajes crudos
print(
    f"La edición ahorra un {dif_final_crudo_otros_cursos}% del tiempo en los cursos promedio"
)
print(f"La edicioón ahorra un {dif_final_crudo_dalto}% del curso de dalto")


print("----------------------------")
print("Equivalentes con otros cursos")
# Equivalente de lo que te da ver diez horas de el curso de dalto en otros cursos
print(
    f"Ver diez horas del curso de dalto equivale a ver {round((otros_cursos_med / curso_de_dalto) * 10, 1)} horas de otros cursos"
)
print(
    f"Ver diez horas otros cursos equivale a ver {round((curso_de_dalto / otros_cursos_med) * 10,1)} horas del curso de dalto"
)
