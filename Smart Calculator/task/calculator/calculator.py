from collections import deque
variable_dict = {}


def declare_variable(i):
    variable_list = i.replace(' ', '').split('=')
    assert variable_list[0].isalpha()
    if len(variable_list) == 2:
        if variable_list[0].isalpha():
            if variable_list[1] in variable_dict:
                variable_dict[variable_list[0]] = variable_dict[variable_list[1]]
            elif int(variable_list[1]):
                variable_dict[variable_list[0]] = variable_list[1]
            return variable_dict
    elif len(variable_list) > 2 or variable_list[1] not in variable_dict:
        print('Invalid assignment')


def calculator(i):
    cal = []
    for x in i:
        if x in variable_dict:
            cal.append(variable_dict[x])
        else:
            cal.append(str(x))
    return eval("".join(cal))

while True:
    inp = input()
    num_list = [int(i) for i in inp if i.isdigit()]
    try:
        if inp == '':
            continue
        elif inp[0] == '/':
            command = inp.replace('/', '')
            if command == 'exit':
                break
            elif command == 'help':
                print('The program calculates the sum of numbers')
            else:
                print('Unknown command')
        elif inp[0].isalpha():
            if '=' in inp:
                declare_variable(inp)
            else:
                print(f"{calculator(inp):.0f}")
        else:
            print(f"{calculator(inp):.0f}")
    except AssertionError:
        print('Invalid identifier')
    except AttributeError:
        print('Invalid identifier')
    except ValueError:
        print('Invalid assignment')
    except NameError:
        print('Unknown variable')
    except SyntaxError:
        print('Invalid expression')
print('Bye!')