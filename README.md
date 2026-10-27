# Conandoydle

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![VS Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Proyecto](https://img.shields.io/badge/Proyecto-Grupal%20Acad%C3%A9mico-6C63FF?style=for-the-badge)

Juego interactivo por consola inspirado en **Wordle**, que utiliza los colores del semáforo para indicar aciertos, aproximaciones o errores directamente en la terminal.

El sistema está estructurado de forma que, a mayor dificultad seleccionada por el usuario, mayor será la cantidad de números que se deben adivinar.

## Cómo se juega

El programa genera un código secreto de dígitos **sin repetir** (del 0 al 9) y tenés **5 intentos** para adivinarlo. Después de cada intento, cada dígito que ingresaste se colorea:

| Color | Significado |
|-------|-------------|
| 🟢 Verde | El número es correcto y está en la posición correcta. |
| 🟡 Amarillo | El número es correcto, pero su posición es incorrecta. |
| 🔴 Rojo | El número no está en el código. |

## Niveles de dificultad

| Opción | Nivel | Dígitos a adivinar |
|--------|-------|--------------------|
| 1 | Fácil | 5 |
| 2 | Intermedio | 6 |
| 3 | Difícil | 7 |

## Cómo ejecutarlo

1. Instalá [Python 3](https://www.python.org/downloads/) si todavía no lo tenés.
2. Descargá este repositorio (botón verde **Code** y luego **Download ZIP**) o copiá el archivo `main.py`.
3. Abrí una terminal en la carpeta del proyecto y ejecutá:

```bash
python main.py
```

En algunos sistemas el comando puede ser `python3 main.py`.

> Para ver bien los colores, usá una terminal con soporte para colores ANSI (la terminal de Windows 10/11, la de Visual Studio Code, o cualquier terminal de Linux o macOS).

## Reglas de entrada

- Se debe ingresar exactamente la cantidad de dígitos del nivel elegido.
- Solo se aceptan números, sin letras.
- No se pueden repetir dígitos en un mismo intento.

## Tecnologías

- Python
- Visual Studio Code

## Sobre el proyecto

💻 Proyecto Final Grupal — Técnicas de Programación | Tecnicatura Superior en Análisis de Sistemas.
