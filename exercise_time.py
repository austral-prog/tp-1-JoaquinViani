def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    horas_totales = total_segundos // 3600
    minutos = (total_segundos % 3600 ) // 60
    segundos_restantes = ((total_segundos % 3600)%60)

    print (horas_totales)
    print (minutos)
    print (segundos_restantes)


