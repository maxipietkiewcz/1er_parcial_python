import pandas as pd
import matplotlib.pyplot as plt


calificaciones = [
{"nombre": "Juan", "matematicas": 85, "ciencias": 90,
"historia": 75},
{"nombre": "María", "matematicas": 70, "ciencias": 80,
"historia": 85},
{"nombre": "Pedro", "matematicas": 95, "ciencias": 75,
"historia": 90},
{"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia":
80},
{"nombre": "Luis", "matematicas": 75, "ciencias": 70,
"historia": 95},
{"nombre": "Sofía", "matematicas": 90, "ciencias": 85,
"historia": 75},
{"nombre": "Carlos", "matematicas": 85, "ciencias": 90,
"historia": 80},
{"nombre": "Elena", "matematicas": 70, "ciencias": 75,
"historia": 85},
{"nombre": "Javier", "matematicas": 80, "ciencias": 85,
"historia": 90},
{"nombre": "Laura", "matematicas": 75, "ciencias": 70,
"historia": 95},
{"nombre": "Diego", "matematicas": 90, "ciencias": 85,
"historia": 75},
{"nombre": "Paula", "matematicas": 85, "ciencias": 90,
"historia": 80},
{"nombre": "Carmen", "matematicas": 70, "ciencias": 75,
"historia": 85}
]

# creamos el dataframe
df = pd.DataFrame(calificaciones, columns=["nombre", "matematicas", "ciencias", "historia"])
print(df)


#Calcular el promedio de calificaciones para cada asignatura y mostrarlo.
print("Promedio matematicas: ",df['matematicas'].mean())
print("Promedio ciencias: ",df['ciencias'].mean())
print("Promedio historia: ", df['historia'].mean())
print()

# Encuentra a los estudiantes que tienen las calificaciones más altas en cada asignatura 
# y mostralos junto con sus respectivas calificaciones. 

calificaciones_maximas_por_asignatura = df.max()

print("Estudiantes con las calificaciones más altas por asignatura:")
for asignatura in df.columns[1:]:
    estudiante = df[df[asignatura] == calificaciones_maximas_por_asignatura[asignatura]]['nombre'].values[0]
    calificacion = calificaciones_maximas_por_asignatura[asignatura]
    print(f"{asignatura}: {estudiante} - {calificacion}")
print()

# Calcular el porcentaje de estudiantes que aprobaron cada asignatura (con una
# calificación igual o superior a 60) y mostrar los resultados.

porcentaje_aprobados_por_asignatura = (df.drop('nombre', axis=1) >= 60).mean() * 100

print("Porcentaje de estudiantes que aprobaron cada asignatura:")
print(porcentaje_aprobados_por_asignatura)
print()


# Calcular el promedio de calificaciones para cada estudiante
df['promedio'] = df[['matematicas', 'ciencias', 'historia']].mean(axis=1)

# Crear un DataFrame con el nombre del estudiante y su promedio de notas
df_promedio = df[['nombre', 'promedio']]

# Mostrar el DataFrame
print("DataFrame con el nombre del estudiante y su promedio de notas:")
print(df_promedio)
print()

# Crear un gráfico de barras 
plt.bar(df_promedio['nombre'], df_promedio['promedio'], color='skyblue') # color de la barra
plt.xlabel('Estudiantes') # etiqueta del eje x
plt.ylabel('Promedio de Calificaciones') # etiqueta del eje y
plt.title('Promedio de Calificaciones por Estudiante') # titulo del grafico
plt.xticks(rotation=45, ha='right') # rotar las etiquetas del eje x
plt.grid(axis='y', linestyle='--', alpha=0.7) # agregar una grilla
plt.tight_layout() # ajustar el tamanio del grafico
plt.show() # mostrar el grafico 
