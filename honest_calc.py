# write your code here
import sys

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
operations = {'+', '-', '*', '/'}
memory = 0
result = 0
x, y = 0.0, 0.0
oper = ''


def check_variables(a, b):
    global x
    global y
    global memory
    try:
        if a == 'M':
            x = memory
        else:
            x = float(a)
        if b == 'M':
            y = memory
        else:
            y = float(b)
    except ValueError:
        print(msg_1)
        return False
    else:
        return True


def is_one_digit(v):
    v = float(v)
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check_digitines_of_variables(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 in operations and v3 != '/'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def check_operator(o):
    global result
    if o not in operations:
        print(msg_2)
        return False
    check_digitines_of_variables(x, y, oper)
    if o == '+':
        result = x + y
    elif o == '-':
        result = x - y
    elif o == '*':
        result = x * y
    elif o == '/' and y != 0:
        result = x / y
    else:
        print(msg_3)
        return False
    return True


def ask_for_variables():
    global x
    global y
    global oper
    while True:
        print(msg_0)
        calc = input()
        x, oper, y = calc.split()
        if not check_variables(x, y):
            continue
        if not check_operator(oper):
            continue
        break


def save_result_to_memory():
    global memory
    msg_ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, msg_10, msg_11, msg_12]
    while True:
        print(msg_4)
        answer4 = input()
        if answer4 == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(msg_[msg_index])
                    answer10 = input()
                    if answer10 == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer10 == 'n':
                        break
                    else:
                        continue
                break
            else:
                memory = result
                break
        elif answer4 == 'n':
            break
        else:
            continue


def continue_calculations():
    while True:
        print(msg_5)
        answer5 = input()
        if answer5 == 'y':
            break
        elif answer5 == 'n':
            sys.exit()
        else:
            continue


if __name__ == "__main__":
    while True:
        ask_for_variables()
        print(float(result))
        save_result_to_memory()
        continue_calculations()
