#import modules
import climage
from termcolor import colored

#defined variables
main = True
menu = True
about = False
begin = False

while main:
    while menu:
#       graphics
        print((colored('\n~ ~ ~~cana9~~ ~ ~', 'cyan', attrs=['underline', 'bold'])))
        print('0. exit program\n1. about the app\n2. begin operations\n')
#       climage conversion from png to ansi image to display in terminal
        cana_pic = climage.convert('cana_pic.png', is_unicode=True, width=20)
        print(cana_pic)
#       menu input
        main_input = input(colored('> ', 'cyan'))
        if main_input == '0':
            quit()
        elif main_input == '1':
            menu = False
            about = True
        elif main_input == '2':
            menu = False
            begin = True
        else:
            pass
#   the 'about' section of the program
    while about:
        print((colored('\n~ ~ ~~about the app~~ ~ ~', 'cyan', attrs=['underline', 'bold', 'reverse'])))
        print('cana9 (which means \'common amazing number adder 9\') is a terminal and client based program\nthat works as a calculator.\nyou can add, multiply, divide and less.\nplease enjoy.\nthis software is open source and licensed under bsd 3-clause.\ncharacter is licensed under cc-by-sa 4.0\n')
        print((colored('\n~ ~ ~~about the character~~ ~ ~', 'cyan', attrs=['underline', 'bold', 'reverse'])))
        print('their name is cana. they are genderless because it that makes it more neutral, like math!! math doesnt care about how its being used\n')
#       another climage conversion, from png to ansi        
        cana_uwu = climage.convert('cana_uwu.png', is_unicode=True, width=20)
        print(cana_uwu)
        print('type \'6\' and \'enter\' to return to the menu')
#       input in the 'about' part
        about_inp = input(colored('> ', 'cyan'))
#       basic parameters, if you type 6 then youll go back to the menu
        if about_inp == '6':
            menu = True
            about = False
        else:
            pass
#   the calculator itself, i mean i doubt a lot of people will read the code but please, please when youre typing the number after being asked the operator. dont put any string on it!! no letters or other characters that arent numbers please
    while begin:
        operator = input((colored('enter an operator (+ - * /): ', 'cyan', attrs=['underline', 'bold', 'reverse'])))
        num1 = float(input(colored('enter the 1st number: ', 'cyan')))
        num2 = float(input(colored('enter the 2nd number: ', 'cyan')))
#       these do the calculations
        if operator == '+':
            result = num1 + num2
            print(result)
        elif operator == '-':
            result = num1 - num2
            print(result)
        elif operator == '*':
            result = num1 * num2
            print(result)
        elif operator == '/':
            result = num1 / num2
            print(result)
        else:
            print(f'{operator} isnt a valid operator')