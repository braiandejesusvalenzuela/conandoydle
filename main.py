import random
import os

os.system('')

# Definición de Colores ANSI
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
TURQUESA = "\033[96m"
LILA_VIOLETA = "\033[95m"  # Para Menú de Dificultad
NARANJA = "\033[38;5;208m" # Para Advertencias, Errores y Despedida
RESET = "\033[0m"

# Círculos completos garantizados en formato ANSI
CIRCULO_ROJO = f"{ROJO}●{RESET}"
CIRCULO_AMARILLO = f"{AMARILLO}●{RESET}"
CIRCULO_VERDE = f"{VERDE}●{RESET}"

def crear_codigo(cant_numeros):
    """Devuelve un texto con la cantidad de numeros que indica cant_numeros, sin repetir"""
    codigo_ia = []
    for v in range(cant_numeros):
        ia = random.randint(0, 9)
        while ia in codigo_ia:
            ia = random.randint(0, 9)
        codigo_ia.append(ia)
    codigo_ia = "".join(map(str, codigo_ia))
    return codigo_ia

def crear_codigo_usuario(cant_numeros):
    """Devuelve el codigo ingresado por el usuario validando longitud y que sean solo digitos"""
    print(f"{TURQUESA}Ingrese su respuesta:{RESET} ", end="")
    codigo = input("")
    while len(codigo) != cant_numeros or not codigo.isdigit():
        print(f"{NARANJA}Error: Debe ingresar exactamente {cant_numeros} digitos y sin letras.{RESET}")
        print(f"{NARANJA}Vuelva a ingresar su respuesta:{RESET} ", end="")
        codigo = input("")
    return codigo

def tiene_repetidos(cod_usuario):
    """Devuelve si el cod_usuario contiene digitos repetidos"""
    for i in range(len(cod_usuario)):
        cont = 0
        for j in range(i, len(cod_usuario)):
            if cod_usuario[i] == cod_usuario[j]:
                cont += 1
        if cont > 1:
            return True
    return False

def comparar_numeros(codigo, codigo_usuario):
    """Devuelve una lista de estados para cada numero que posee codigo_usuario"""
    lista_estados = []
    for i in range(len(codigo_usuario)):
        if codigo[i] == codigo_usuario[i]:
            lista_estados.append("Lugar")
        else:
            cont = 0
            for j in range(len(codigo)):
                if codigo_usuario[i] == codigo[j]:
                    cont += 1
            if cont > 0:
                lista_estados.append("Numero")
            else:
                lista_estados.append("Nada")
    return lista_estados

def pintar_codigo_usuario(lista_estados, codigo_usuario):
    """Imprime con el color asignado a cada elemento de codigo_usuario"""
    for i in range(len(lista_estados)):
        texto = ""
        if lista_estados[i] == "Lugar":
            texto += VERDE
        elif lista_estados[i] == "Numero":
            texto += AMARILLO
        else:
            texto += ROJO
        texto += codigo_usuario[i]
        texto += RESET
        print(texto, end="")
    print('')

def mostrar_final(ha_ganado, turnos):
    """Imprime el resultado de la partida"""
    if ha_ganado:
        # Mensaje de victoria en verde
        print(f"\n{VERDE}¡¡¡Ganaste en {turnos} turno(s)!!!{RESET}")
    else:
        # Mensaje de derrota en rojo
        print(f"\n{ROJO}Se te acabaron los intentos. Perdiste.{RESET}")

def elegir_dificultad(dificultad_base):
    """Solicita la dificultad con opciones y confirmación en Lila/Violeta"""
    ingreso = 0
    while ingreso not in ["1", "2", "3"]:
        print(f"\n{TURQUESA}Ingrese el nivel de dificultad:{RESET}\n"
              f"{LILA_VIOLETA}1 - Facil: 5 digitos{RESET}\n"
              f"{LILA_VIOLETA}2 - Intermedio: 6 digitos{RESET}\n"
              f"{LILA_VIOLETA}3 - Dificil: 7 digitos{RESET}\n"
              f"{NARANJA}*Ten en cuenta que son 5 intentos.{RESET}")
        ingreso = input("Su eleccion: ")

    # Muestra "Dificultad seleccionada" y el número ingresado en Lila/Violeta
    print(f"{LILA_VIOLETA}Dificultad seleccionada: {ingreso}{RESET}\n")
    return dificultad_base + int(ingreso)

def jugar():
    """Ciclo principal de una partida"""
    intentos = 5
    digitos = elegir_dificultad(4)
    codigo_secreto = crear_codigo(digitos)
    contador = 0
    codigo_us = ""
    
    while contador < intentos and codigo_us != codigo_secreto:
        print(f'{TURQUESA}Te quedan {intentos - contador} intento/s{RESET}')
        codigo_us = crear_codigo_usuario(digitos)
        while tiene_repetidos(codigo_us):
            print(f'{NARANJA}No se pueden ingresar digitos repetidos.{RESET}')
            codigo_us = crear_codigo_usuario(digitos)
            
        pintar_codigo_usuario(comparar_numeros(codigo_secreto, codigo_us), codigo_us)
        contador += 1
        
    mostrar_final(codigo_secreto == codigo_us, contador)

def jugar_nuevamente():
    """Consulta al usuario si desea volver a jugar en color Turquesa"""
    j = ''
    while j not in ['si', 'no']:
        j = input(f'\n{TURQUESA}¿Quiere jugar de nuevo? (si/no):{RESET} ').lower()
    return j == 'si'

# --- INICIO DEL PROGRAMA ---

# Título con círculos llenos en color ANSI
print(f"{CIRCULO_ROJO}  {CIRCULO_AMARILLO}  {CIRCULO_VERDE}  {TURQUESA}Conandoydle - Adivina el codigo secreto{RESET}\n")
print(f"Bienvenido/a al {TURQUESA}Conandoydle{RESET}\n")

# Instrucciones
print(f"{TURQUESA}Instrucciones:{RESET} Debe adivinar un numero, los digitos que puede "
      'ingresar son entre 0-9, tiene 5 intentos y los numeros no se pueden repetir.\n'
      'En su ingreso se van a colorear los digitos indicando:\n'
      f'- {CIRCULO_VERDE} {VERDE}Verde:{RESET} El numero es el correcto y se encuentra en la posicion correspondiente.\n'
      f'- {CIRCULO_AMARILLO} {AMARILLO}Amarillo:{RESET} El numero es correcto pero su posicion es incorrecta.\n'
      f'- {CIRCULO_ROJO} {ROJO}Rojo:{RESET} El numero no es correcto.')

# Bucle del juego
jugar()
while jugar_nuevamente():
    jugar()

# Mensaje final en Naranja
print(f'\n{NARANJA}¡Gracias por jugar!{RESET}')
