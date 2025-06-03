import os

def ingresar_datos():
    estudiantes = {}
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        try:
            notas_str = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones = list(map(float, notas_str.split(',')))
            estudiantes[nombre] = calificaciones
        except ValueError:
            print("Error: asegúrate de ingresar solo números separados por comas.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {}
    for nombre, calificaciones in estudiantes.items():
        if calificaciones:
            promedio = sum(calificaciones) / len(calificaciones)
        else:
            promedio = 0
        promedios[nombre] = promedio
    return promedios

def encontrar_mejor_estudiante(promedios):
    if not promedios:
        return None, 0
    mejor = max(promedios, key=promedios.get)
    return mejor, promedios[mejor]

def guardar_en_archivo(estudiantes, promedios, mejor_estudiante, mejor_promedio):
    
    ruta_directorio = "/home/devasc/labs/devnet-src/python/practpython" 
    os.makedirs(ruta_directorio, exist_ok=True)  

    ruta_archivo = os.path.join(ruta_directorio, "resultados.txt")

    with open(ruta_archivo, "w") as archivo:
        archivo.write("Datos de estudiantes y promedios:\n")
        for nombre in estudiantes:
            archivo.write(f"{nombre}: Calificaciones: {estudiantes[nombre]} - Promedio: {promedios[nombre]:.2f}\n")
        archivo.write(f"\nEstudiante con el mejor promedio: {mejor_estudiante} ({mejor_promedio:.2f})\n")

    print(f"Datos guardados en: {ruta_archivo}")

def main():
    estudiantes = ingresar_datos()
    if not estudiantes:
        print("No se ingresaron datos.")
        return
    promedios = calcular_promedios(estudiantes)
    mejor_estudiante, mejor_promedio = encontrar_mejor_estudiante(promedios)
    guardar_en_archivo(estudiantes, promedios, mejor_estudiante, mejor_promedio)

if __name__ == "__main__":
    main()

