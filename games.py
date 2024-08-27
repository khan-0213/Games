import random


def calculator():
    print("--->Kalkulator<---")
    print('''
    Kalkulatorni ishlatish uchun avval son 
    keyin amal keyin yana son kiritiladi 
    ular orasida prabel bo'lsin.''')
    print('''
        '+' => qo'shish.
        '-' => ayirish.
        '*' => ko'paytirish.
        '/' => bo'lish.
        '//' => bo'linmaning butun qismi.
        '%' => bo'linmaning qoldiq qismi.
        Shu amallardan birontasini kiriting.
        Dasturni to'xtatish uchun 'no' ni kiriting.
    ''')
    ishora = True
    while ishora:
        qiymat = input('Qiymatlar >>> ').split()
        if qiymat[0] == 'no':
            ishora = False
        elif (type(int(qiymat[0])) == int or type(float(qiymat[0])) == float) and (type(int(qiymat[2])) == int or type(float(qiymat[2])) == float):
            if qiymat[1] == '+':
                print(float(qiymat[0]) + float(qiymat[2]))
            elif qiymat[1] == '-':
                print(float(qiymat[0]) - float(qiymat[2]))
            elif qiymat[1] == '*':
                print(float(qiymat[0]) * float(qiymat[2]))
            elif qiymat[1] == '/':
                if float(qiymat[2]) != 0:
                    print(float(qiymat[0]) / float(qiymat[2]))
                else:
                    print('Sonni nolga bo\'lib bo\'lmaydi!')
            elif qiymat[1] == '//':
                if float(qiymat[2]) != 0:
                    print(float(qiymat[0]) // float(qiymat[2]))
                else:
                    print('Sonni nolga bo\'lib bo\'lmaydi!')
            elif qiymat[1] == '%':
                if float(qiymat[2]) != 0:
                    print(float(qiymat[0]) % float(qiymat[2]))
                else:
                    print('Sonni nolga bo\'lib bo\'lmaydi!')
        else:
            print('Error')
    print('Dastur to\'xtadi.')


def calculator_game():
    amal = ['+', '-', '*', '/']
    ishora = True
    while ishora:
        print('--->Calculator Game<---')
        print('''
        Daraja tanlang => 1, 2, 3, 4;
            1. Oson.
            2. O'rtacha.
            3. Qiyin.
            4. O'yinni to'xtatish.
        ''')
        daraja = input('Daraja: >>> ')
        if int(daraja) == 1:
            print("O'yinni to'xtatish uchun 'no' ni kiriting.")
            ishora1 = True
            while ishora1:
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                o = random.choice(amal)
                javob = input(f'{x} {o} {y} = ')
                if javob == 'no':
                    ishora1 = False
                elif o == '+':
                    if x + y == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '-':
                    if x - y == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '*':
                    if x * y == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '/':
                    if y != 0:
                        if x // y == int(javob):
                            print("To'g'ri!")
                        else:
                            print('Xato.')
                    else:
                        print('Error')
            print("O'yin tugadi.")
        elif int(daraja) == 2:
            print("O'yinni to'xtatish uchun 'no' ni kiriting.")
            ishora2 = True
            while ishora2:
                x = random.randint(1, 30)
                y = random.randint(1, 30)
                o = random.choice(amal)
                javob = input(f'{x} {o} {y} = ')
                if javob == 'no':
                    ishora2 = False
                elif o == '+':
                    if x + y == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '-':
                    if x - y == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '*':
                    if x * y == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '/':
                    if y != 0:
                        if x // y == int(javob):
                            print("To'g'ri!")
                        else:
                            print('Xato.')
                    else:
                        print('Error')
            print("O'yin tugadi.")
        elif int(daraja) == 3:
            print("O'yinni to'xtatish uchun 'no' ni kiriting.")
            ishora3 = True
            while ishora3:
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                z = random.randint(1, 10)
                o = random.choice(amal)
                o1 = random.choice(amal)
                javob = input(f'{x} {o} {y} {o1} {z} = ')
                if javob == 'no':
                    ishora3 = False
                elif o == '+' and o1 == '+':
                    if x + y + z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '+' and o1 == '-':
                    if x + y - z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '+' and o1 == '*':
                    if x + y * z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '+' and o1 == '/':
                    if x + y / z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '-' and o1 == '+':
                    if x - y + z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '-' and o1 == '-':
                    if x - y - z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '-' and o1 == '*':
                    if x - y * z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '-' and o1 == '/':
                    if x - y / z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '*' and o1 == '+':
                    if x * y + z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '*' and o1 == '-':
                    if x * y - z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '*' and o1 == '*':
                    if x * y * z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '*' and o1 == '/':
                    if x * y / z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '/' and o1 == '+':
                    if x // y + z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '/' and o1 == '-':
                    if x // y - z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '/' and o1 == '*':
                    if x // y * z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
                elif o == '/' and o1 == '/':
                    if x // y // z == int(javob):
                        print("To'g'ri!")
                    else:
                        print('Xato.')
            print("O'yin tugadi.")
        else:
            ishora = False
    print("O'yin to'xtadi.")


def son_top():
    print("Kompyuter 0 dan 10 oralig'ida son o'ylaydi. Siz bu sonni topishingiz kerak.")
    ishora = True
    while ishora:
        taxminlar = 0
        play = input("O'yinni davom etirasizmi? \n{'yes' / 'no'} >>> ")
        if play == 'no':
            ishora = False
        else:
            k_oylagan_son = random.randint(1, 10)
            while True:
                taxminlar += 1
                taxmin = input('Taxminingiz: >>>')
                if k_oylagan_son > int(taxmin):
                    print(f"{taxmin} dan kattaroq.")
                elif k_oylagan_son < int(taxmin):
                    print(f"{taxmin} dan kichikroq.")
                else:
                    break
            print(f"Barakalla siz {taxminlar} urinishda topdingiz!!!")
    print("O'yin tugadi.")


def son_oyla():
    print("Men 1 dan 10 oralig'ida son o'ylayman. Sen topishing kerak.")
    ishora = True
    while ishora:
        print("O'yinni davom etirasizmi?")
        play = input("{yes / no } >>>")
        if play == 'no':
            ishora = False
        else:
            taxminlar = 0
            boshi = 0
            oxiri = 10
            while True:
                taxminlar += 1
                taxmin = random.randint(boshi, oxiri)
                javob = input(f"Agar javob {taxmin} bo'lsa 't', kichik bo'lsa 'k', katta bo'lsa 'K' ni kiriting.")
                if javob == 't':
                    print(f"Men {taxminlar} urinish bilan topdim.")
                    break
                elif javob == 'k':
                    oxiri = taxmin - 1
                elif javob == 'K':
                    boshi = taxmin + 1
    print("O'yin tugadi.")


def tosh_qaychi_qogoz():
    qiymat = ['tosh', 'qaychi', "qog'oz"]
    print("Tosh, qaychi, qog'oz o'yini ")
    ishora = True
    while ishora:
        print("Oyinni davom etirasizmi?")
        play = input("{'yes'/'no'} >>> ")
        if play == 'no':
            ishora = False
        else:
            kompyuter = random.choice(qiymat)
            men = input("'tosh', 'qaychi', 'qog'oz'\nTanlovingizni kiriting: >>> ")
            if kompyuter == men:
                print(f'Kompyuter: >>> {kompyuter}\nDurrang.')
            elif kompyuter == 'tosh':
                print(f'Kompyuter: >>> {kompyuter}\nKompyuter yutdi.')
            elif kompyuter == "qog'oz":
                print(f'Kompyuter: >>> {kompyuter}\nMen yutdim.')
            elif kompyuter == 'qaychi' and men == 'qog\'oz':
                print(f'Kompyuter: >>> {kompyuter}\nKompyuter yutdi.')
            elif men == 'tosh':
                print(f'Kompyuter: >>> {kompyuter}\nmen yutdim.')
            elif men == 'qog\'oz':
                print(f'Kompyuter: >>> {kompyuter}\nkompyuter yutdi.')
    print("O'yin tugadi.")


def games():
    ishora = True
    while ishora:
        print('''
            Assalomu Aleykum!!!
            Qaysi o'yinni o'ynamoqchisiz?
            ----------------------------
            1. Calculator ammallarni hisoblaydi.
            2. Calculator_game o'yini.
            3. Son_top o'yini.
            4. Son_o'yla o'yini.
            5. Tosh_qaychi_qog'oz o'yini
            6. Chiqish.
        ''')
        play = input("O'yinni tanlang: >>> ")
        if int(play) == 1:
            calculator()
        elif int(play) == 2:
            calculator_game()
        elif int(play) == 3:
            son_top()
        elif int(play) == 4:
            son_oyla()
        elif int(play) == 5:
            tosh_qaychi_qogoz()
        elif int(play) == 6:
            break
        else:
            print("Noto'g'ri qiymat kiritdingiz.")


if __name__ == '__main__':
    games()
