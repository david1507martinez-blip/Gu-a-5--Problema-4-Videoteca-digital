#Nombre del estudiante:CRISTIAN DAVID MARTINEZ PINILLA
#Grupo:(213022B_2201)
#Programa:Ingenerìa Electrònica
#Autoria Propia

# Problema 4:  Una videoteca digital 

def contar_titulos_populares_recientes(matriz, umbral_calificacion, anio_limite):
    """
    Cuenta los títulos que cumplen con:
    - Calificación >= umbral_calificacion
    - Año de lanzamiento >= anio_limite
    
    Args:
        matriz: Lista de listas con [Título, Año, Calificación, Género]
        umbral_calificacion: Número mínimo de calificación (int o float)
        anio_limite: Año mínimo de lanzamiento (int)
    
    Returns:
        int: Cantidad de títulos que cumplen ambos criterios
    """
    contador = 0
    
    for titulo in matriz:
        # Extraer los datos de cada título
        nombre = titulo[0]
        anio = titulo[1]
        calificacion = titulo[2]
        genero = titulo[3]
        
        # Verificar si cumple con ambos criterios
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            contador += 1
            print(f"✓ {nombre} ({anio}) - Calificación: {calificacion} - Género: {genero}")
    
    return contador


def main():
    # Crear la matriz con al menos 7 títulos
    videoteca = [
        ["Inception", 2010, 8.8, "Ciencia Ficción"],
        ["Parasite", 2019, 9.0, "Thriller"],
        ["The Godfather", 1972, 9.2, "Drama"],
        ["Spider-Man: No Way Home", 2021, 8.2, "Acción"],
        ["The Dark Knight", 2008, 9.0, "Acción"],
        ["Encanto", 2021, 7.8, "Animación"],
        ["Dune", 2021, 8.5, "Ciencia Ficción"]
    ]
    
    # Mostrar todos los títulos disponibles
    print("=== VIDEOTECA DIGITAL ===\n")
    print("Catálogo completo:")
    print("-" * 60)
    for titulo in videoteca:
        print(f"Título: {titulo[0]:25} | Año: {titulo[1]} | Calificación: {titulo[2]} | Género: {titulo[3]}")
    
    # Definir criterios de búsqueda
    print("\n" + "=" * 60)
    print("CRITERIOS DE BÚSQUEDA:")
    umbral_calificacion = 8.0  # Calificación mínima
    anio_limite = 2015         # Año límite mínimo
    print(f"• Calificación mínima: {umbral_calificacion}")
    print(f"• Año mínimo: {anio_limite}")
    
    # Realizar el conteo
    print("\n" + "=" * 60)
    print("TÍTULOS QUE CUMPLEN CON LOS CRITERIOS:")
    print("-" * 60)
    
    cantidad = contar_titulos_populares_recientes(videoteca, umbral_calificacion, anio_limite)
    
    # Mostrar resultado
    print("\n" + "=" * 60)
    print(f"RESULTADO: {cantidad} título(s) cumplen con ambos criterios")
    print("=" * 60)


# Ejecutar el programa
if __name__ == "__main__":
    main()