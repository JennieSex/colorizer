class White(str):
    pass
class Black(str):
    pass
class Red(str):
    pass
class Purple(str):
    pass
class Blue(str):
    pass
class Yellow(str):
    pass
class Cyan(str):
    pass

K: Black = "\u001B[30m"
R: Red = "\u001B[31m"
G: Green = "\u001B[32m"
Y: Yellow = "\u001B[33m"
B: Blue = "\u001B[34m"
P: Purple = "\u001B[35m"
C: Cyan = "\u001B[36m"
W: White = "\u001B[37m"

def colorize(text: str, color: Color) -> str:
    "Colorizing text in console adding ANSI color codes"
    return color + text + "\u001B[0m"
