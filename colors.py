"""This is my colors module.

Whatever
"""

base00 = '\033[1;33m'
base03 = '\033[1;30m'
base02 = '\033[0;30m'
base01 = '\033[1;32m'
base0 = '\033[1;34m'
base1 = '\033[1;36m'
base2 = '\033[0;37m'
base3 = '\033[1;37m'
yellow = '\033[0;33m'
orange = '\033[1;31m'
red = '\033[0;31m'
magenta = '\033[0;35m'
violet = '\033[1;35m'
blue = '\033[0;34m'
cyan = '\033[0;36m'
green = '\033[0;32m'
reset = '\033[0m'
clear = '\033[H\033[2J'
import random
def random_color():
    return random.choice([yellow, orange, red, magenta, violet, blue, cyan, green])
if __name__ == '__main__':
    print(clear)
    print(base03 + 'Base03' + reset, end=' ')
    print(base02 + 'Base02' + reset, end=' ')
    print(base01 + 'Base01' + reset, end=' ')
    print(base00 + 'Base00' + reset, end=' ')
    print(base0 + 'Base0' + reset, end=' ')
    print(base1 + 'Base1' + reset, end=' ')
    print(base2 + 'Base2' + reset, end=' ')
    print(base3 + 'Base3' + reset, end=' ')
    print(red + 'red' + reset, end=' ')
    print(orange + 'orange' + reset, end=' ')
    print(magenta + 'yellow' + reset, end=' ')
    print(violet + 'violet' + reset, end=' ')
    print(cyan + 'cyan' + reset, end=' ')
    print(green + 'green' + reset, end=' ')
    for count in range(7):
        print(random_color() + 'Random' + reset, end=' ')
        print()
