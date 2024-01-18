
# Puntuacion media


# Estado del programa - No me se aun otra forma de como hacer que pare

estado = True

# Asignaturas

asignaturas = []

# Cantidad de alumnos

alumnos = int(input("Insertar la cantidad de alumnos que seran encuestados: "))

# Cantidad de asignaturas

cantidadMaterias = int(input("\nIngresa la cantidad de asignaturas que tiene la Universidad: "))  

# Notas de las asignaturas

notasAsignaturas = []


while estado:
    print("\nBienvenid@s a la Universidad\n")
    
    # For para la cantidad de materias 
    
    for i in range(1, cantidadMaterias + 1):
        asignatura = str(input(f"Ingresa la asignatura numero {i} de la Universidad: "))
        asignaturas.append(asignatura)
    
    print("\nLas asignaturas que tiene la Universidad son las siguientes:\n")
    for i in range(0, cantidadMaterias):
        print("> " + asignaturas[i])
        
    # For para la cantidad de alumnos que van a ser encuestados y de las materias que seran encuestadas
    
    for i in range(0, cantidadMaterias):
        
        print(f"\nLa asignatura {asignaturas[i]} sera encuestada por todos los alumnos")
        
        for j in range(1, alumnos + 1):
            
            print(f"\nEl alumno numero {j} va a poner la nota que tiene en la asignatura {asignaturas[i]}")
            
            notaAsignatura = float(input("Ingresa la nota de la asignatura: "))

            notasAsignaturas.append(notaAsignatura)
    
    # Cambia el estado a False y se termina el ciclo
    
    estado = not estado
    

# total = 0
# suspendidos = 0
# listaGeneral = []

# Aqui va el for para hacer lo ultimo que es mostrar cada materia por separaado con sus notas

print("'Estos son los resultados del semestre'\n")
print("#-------------------------------------------------------------------------------------------------------------------------------------------------------#")
for i in range(0, len(asignaturas)):
    total = 0
    suspensos = 0
    listaGeneral = []
    for j in range(0, len(notasAsignaturas)):
        if (notasAsignaturas[0] < 3):
            suspensos += 1
        nota = notasAsignaturas.pop(0)
        total += nota
        if (j  == alumnos - 1):
            total = total / alumnos
            listaGeneral.append(f"{asignaturas[i]}, {alumnos} alumnos. Nota media: {round(total, 2)}, Suspensos: {suspensos}")
            print()
            print(listaGeneral)
            break
print("#-------------------------------------------------------------------------------------------------------------------------------------------------------#")
