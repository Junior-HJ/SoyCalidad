class SoyCalidad:
    
    def __init__(self) -> None:
        pass
    
    def pregunta_1(self, matriz):
        # Se tiene una matriz nxn de enteros, crear una funcion que
        # retorne un arreglo cuyo primer elemento es la cantidad de
        # números que aparecen solo una vez y cuyo segundo elemento
        # la cantidad de terminos repetidos.
        # Ejemplos
        # [[2, 2], [2, 2]] - [0, 1]
        # [[2, 1, 3], [4, 5, 2], [6, 6, 6]] - [4, 2]
        conteo = {}
        for fila in matriz:
            for numero in fila:
                conteo[numero] = conteo.get(numero, 0) + 1

        unicos = sum(1 for cantidad in conteo.values() if cantidad == 1)
        repetidos = sum(1 for cantidad in conteo.values() if cantidad > 1)

        return [unicos, repetidos]

    def pregunta_2(self, n):
        # Se tiene un número natural n, crear una función que retorne
        # una lista de todos los pares de números naturales que sumen
        # el número n. ( n < 10^6 )
        if n<= 0 or n >= 10**6:
            return []
        
        resultado = []
        
        for i in range(1, n // 2 + 1):
            j = n - i
            resultado.append([i, j])
        
        return resultado

print("=== Prueba técnica ===")

soy_calidad = SoyCalidad()

print("--- Prueba pregunta 1 ---")
print(f"Respuesta Pregunta 1:{soy_calidad.pregunta_1([[2, 2], [2, 2]])}") # [0, 1]

print(f"Respuesta Pregunta 1: {soy_calidad.pregunta_1([[2, 1, 3], [4, 5, 2], [6, 6, 6]])}") # [4, 2]

print("--- Prueba pregunta 2 ---")
print(f"Respuesta Pregunta 2:{soy_calidad.pregunta_2(11)}") # [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]

print("=== Fin prueba técnica ===\n")

print("=== Pruebas unitarias ===")
