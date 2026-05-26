#Nombre del estudiante:CRISTIAN DAVID MARTINEZ PINILLA
#Grupo:(213022B_2201)
#Programa:Ingenerìa Electrònica
#Autoria Propia

# Problema 4:  Una videoteca digital 

def contar_titulos_por_criterios(matriz, umbral_calificacion, anno_limite):
    """
    Cuenta los títulos que cumplen con:
    - Calificación >= umbral_calificacion
    - Año de lanzamiento >= anno_limite
    
    Parámetros:
    matriz: lista de listas con estructura [Título, Año, Calificación, Género]
    umbral_calificacion: número (int o float) mínimo de calificación
    anno_limite: número (int) mínimo de año
    
    Retorna:
    int: cantidad de títulos que cumplen ambos criterios
    """
    contador = 0
    
    for titulo in matriz:
        # Validar que la fila tenga la estructura correcta
        if len(titulo) >= 4:
            titulo_nombre = titulo[0]
            anno = titulo[1]
            calificacion = titulo[2]
            genero = titulo[3]
            
            # Verificar ambos criterios
            if calificacion >= umbral_calificacion and anno >= anno_limite:
                contador += 1
                print(f"✓ Cumple: {titulo_nombre} ({anno}) - Calificación: {calificacion} - Género: {genero}")
    
    return contador


def main():
    # Crear matriz con al menos 7 títulos
    # Formato: [Título, Año de Lanzamiento, Calificación (1-10), Género]
    videoteca = [
        ["El Padrino", 1972, 9.5, "Drama"],
        ["Interestelar", 2014, 8.9, "Ciencia Ficción"],
        ["Parásitos", 2019, 9.0, "Thriller"],
        ["El Caballero de la Noche", 2008, 9.2, "Acción"],
        ["Dune: Parte Dos", 2024, 8.7, "Ciencia Ficción"],
        ["Oppenheimer", 2023, 9.1, "Drama Histórico"],
        ["Barbie", 2023, 7.8, "Comedia"],
        ["Spider-Man: Un Nuevo Universo", 2018, 8.6, "Animación"],
        ["John Wick 4", 2023, 8.5, "Acción"]
    ]
    
    # Configurar criterios de búsqueda
    print("=== BUSCADOR DE TÍTULOS POPULARES Y RECIENTES ===\n")
    
    umbral_calificacion = 8.5  # Calificación mínima requerida
    anno_limite = 2020         # Año mínimo de lanzamiento
    
    print(f"📊 Criterios de búsqueda:")
    print(f"   • Calificación mínima: {umbral_calificacion}")
    print(f"   • Año mínimo: {anno_limite}\n")
    
    print("📋 Títulos que cumplen los criterios:")
    print("-" * 60)
    
    # Llamar a la función para contar títulos que cumplen los criterios
    cantidad = contar_titulos_por_criterios(videoteca, umbral_calificacion, anno_limite)
    
    print("-" * 60)
    print(f"\n✅ TOTAL DE TÍTULOS QUE CUMPLEN AMBOS CRITERIOS: {cantidad}\n")
    
    # También podemos mostrar información adicional
    print("📈 Estadísticas adicionales:")
    print(f"   Total de títulos en videoteca: {len(videoteca)}")
    porcentaje = (cantidad / len(videoteca)) * 100
    print(f"   Porcentaje que cumple criterios: {porcentaje:.1f}%")


# Función adicional para probar con diferentes criterios
def probar_diferentes_criterios():
    """Función para probar el buscador con diferentes umbrales"""
    
    videoteca = [
        ["El Padrino", 1972, 9.5, "Drama"],
        ["Interestelar", 2014, 8.9, "Ciencia Ficción"],
        ["Parásitos", 2019, 9.0, "Thriller"],
        ["El Caballero de la Noche", 2008, 9.2, "Acción"],
        ["Dune: Parte Dos", 2024, 8.7, "Ciencia Ficción"],
        ["Oppenheimer", 2023, 9.1, "Drama Histórico"],
        ["Barbie", 2023, 7.8, "Comedia"]
    ]
    
    print("\n=== PRUEBA CON DIFERENTES CRITERIOS ===\n")
    
    casos_prueba = [
        (8.0, 2020, "Calificación alta y años recientes"),
        (9.0, 2000, "Calificación muy alta desde 2000"),
        (7.5, 2023, "Calificación aceptable en últimos años"),
        (9.5, 1970, "Calificación perfecta histórica")
    ]
    
    for calif, anno, descripcion in casos_prueba:
        print(f"\n🔍 {descripcion}:")
        print(f"   Umbral calificación: {calif}, Año límite: {anno}")
        cantidad = contar_titulos_por_criterios(videoteca, calif, anno)
        print(f"   ➜ Resultado: {cantidad} título(s) cumplen\n")
