import enum
import sys
import time

TEXTO = (
    "Animação de máquina de escrever, como o nome sugere, é um efeito que se parece com \n"
    "uma animação de digitação, como sendo digitado por uma máquina de escrever. \n "
    "Vamos criar essa animação sem JavaScript, HTML ou CSS. \n Apenas usando o PYTHON!"
)


class Velocity(enum.Enum):
    NORMAL = 0
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    ULTRAFAST = 4


class TypeWriter:
    @classmethod
    def show_letter_by_letter(cls, velocity=Velocity.NORMAL):
        i_wait = 0
        if velocity == Velocity.NORMAL:
            i_wait = 0
        elif velocity == Velocity.SLOW:
            i_wait = 0.45
        elif velocity == Velocity.MEDIUM:
            i_wait = 0.30
        elif velocity == Velocity.FAST:
            i_wait = 0.15
        elif velocity == Velocity.ULTRAFAST:
            i_wait = 0.1

        colors = ["\033[34m", "\033[31m"]  # Azul e Vermelho
        color_index = 0

        for letra in TEXTO:
            sys.stdout.write(colors[color_index] + letra + "\033[0m")
            sys.stdout.flush()
            time.sleep(i_wait)

            color_index = (color_index + 1) % len(colors)

        sys.stdout.write("\n")  # Pula para a próxima linha após terminar


TypeWriter.show_letter_by_letter(Velocity.ULTRAFAST)
