def h():
    print("Hello, world!")

def y():
    print("Hello! My name is Hyunsung-Kim, the maker of hyun99lang.")
    print("Well... Actually I got nothing to say.")
    print("I just wanted to make a language even if it's not very useful.")
    print("I hope you like this.")

def u(string):
    temp_string = ''
    for i in string:
        temp_string += i
    print(temp_string)


def n():
    # calculator
    calc = list(input("수식을 입력하세요(연산자는 띄어쓰기로 구분, 하나의 연산자만 사용, 예: 3 + 5): ").split())
    if calc[1] == '+':
        print("답:", float(calc[0]) + float(calc[2]))
    elif calc[1] == '-':
        print("답:", float(calc[0]) - float(calc[2]))
    elif calc[1] == '*':
        print("답:", float(calc[0]) * float(calc[2]))
    elif calc[1] == '/':
        print("답:", float(calc[0]) / float(calc[2]))
    elif calc[1] == '%':
        print("답:", float(calc[0]) % float(calc[2]))
    else:
        print("입력이 잘못되었습니다. 다시 입력해주세요!")
        n()
    

def bottles():
    for i in range(99, 2, -1):
        print(i, 'bottles of beer on the wall,', i, 'bottles of beer.')
        print('Take one down and pass it around,', i-1, 'bottles of beer on the wall.')

    print('2 bottles of beer on the wall, 2 bottles of beer.')
    print('Take one down and pass it around, 1 bottle of beer on the wall.')

    print('1 bottle of beer on the wall, 1 bottle of beer.')
    print('Take one down and pass it around, no more bottles of beer on the wall.')

    print('No more bottles of beer on the wall, no more bottles of beer.')
    print('Go to the store and buy some more, 99 bottles of beer on the wall.')

while True:
    finish = False
    code = list(input("code: "))

    i = 0
    print("")
    while i < len(code):
        if code[i] == ' ':
            i += 1
            continue

        elif code[i] == 'h':
            h()
            print("")

        elif code[i] == 'y':
            y()
            print("")

        elif code[i] == 'u' and code[i+1] == '-':
            i += 2
            temp_i = i
            while code[i] != '-':
                i += 1

            u(code[temp_i:i])
            print("")

        elif code[i] == 'n':
            n()
            print("")

        elif code[i] == '9' and code[i+1] == '9':
            i += 1
            bottles()
            print("")

        elif code[i] == 'q':
            finish = True
            break

        else:
            i += 1
            continue

        i += 1
    
    if finish:
        print("hyun99lang is closing...")
        break