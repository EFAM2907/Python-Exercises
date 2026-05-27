

#print('en que año naciste bro, ')
#age = input()

#print(f'que año de mierda, {age}')


curso_actual = 1.5
otros_cursos_maximo= 7
otros_cursos_min= 2.5
otros_cursos_promedio=4


#crudos o videos sin editar

video_promedio_sin_edit = 5
video_promedio_sin_edit_curso_actual = 3.5

#porcentaje_materil_inservible_promedio = 100 - otros_cursos_promedio / video_promedio_sin_edit * 100
porcentaje_materil_inservible_promedio = 100 - otros_cursos_promedio / video_promedio_sin_edit * 100


print(porcentaje_materil_inservible_promedio)



diferencia_porcentaje_min = 100 - curso_actual / otros_cursos_min * 100
diferencia_porcentaje_max = 100 - curso_actual / otros_cursos_maximo * 100
diferencia_porcentaje_promedio= 100 -curso_actual / otros_cursos_promedio * 100

#print(diferencia_porcentaje_max)




#print(f'curso actual es un {diferencia_porcentaje_min} mas rapido que el curso mas rapido')
#print(f'curso actual es un {diferencia_porcentaje_max} mas rapido que el curso mas lento')
#print(f'curso actual es un {diferencia_porcentaje_promedio} mas rapido que el curso mas promedio')