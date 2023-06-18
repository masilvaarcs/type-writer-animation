# import sys
# import os
import time
import enum

texto = "Animação de máquina de escrever, como o nome sugere, \n é um efeito que se parece com uma animação de " \
        "digitação, \n como sendo digitado por uma máquina de escrever. \n Vamos criar essa animação sem JavaScript, " \
        "HTML ou CSS. \n Apenas usando o PYTHON!"


class Velocity(enum.Enum):
    normal = 0
    slow = 1
    medium = 2
    fast = 3
    ultrafast = 4


def show_letter_by_letter(partexto='', velocity=Velocity.normal):
    i_wait = 0
    if velocity == Velocity.normal:
        i_wait = 0

    elif velocity == Velocity.slow:
        i_wait = 0.45

    elif velocity == Velocity.medium:
        i_wait = 0.30

    elif velocity == Velocity.fast:
        i_wait = 0.15

    elif velocity == Velocity.ultrafast:
        i_wait = 0.1

    for letra in partexto:
        # sys.stdout.write(letra)
        # sys.stdout.flush()
        print(letra, end='', flush=True)
        if letra != "\n":
            time.sleep(i_wait)
        else:
            time.sleep(1)


show_letter_by_letter(texto, Velocity.ultrafast)
