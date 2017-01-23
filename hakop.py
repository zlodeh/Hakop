import random


def maximalnoe(min):
    while True:
        max = input()
        try:
            max = int(max)
            if  bolshe(min, max):
                return max
        except ValueError:
            print("Ошибка, повтороно ведите максимальное число")

def bolshe(min, max):
    if min > max:
        print("Ваше максимальное число меньше минимальной, ведите повторно")
        return False
    elif min == max:
        print("Ваше минимальное число равно максимальной ведите повторно")
        return False
    else:
        return True
def proverka():
    while True:
        cifra = input()
        try:
            return int(cifra)
        except ValueError:
            print("Ошибка, повторно ведите целое число")



print("Ведите миниимальное число")
min = proverka()
print("Ведите максимальное число")
max = maximalnoe(min)
vedeno = random.randint(min,max)
print("Угадайте случайно число в диопозоне от", min,"до", max, "которое выведит программа")

while True:
    chislo = proverka()
    if not ( min < chislo and chislo < max):
        print("Ваше число не входит диапозон, ведите повторно")
        continue
    else:
        if chislo != vedeno:
            print("не угадали))) еще раз")
            if chislo > vedeno:
                print("Ваше число больше")
                continue
            else:
                print("Ваше число меньше")
                continue
        else:
            print("Вы угадали")
            break
