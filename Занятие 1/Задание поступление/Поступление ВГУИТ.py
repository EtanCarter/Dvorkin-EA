# -*- coding: utf-8 -
age = int(input())
name = input()
if name == "Иван":
    print("Ошибка")
elif age >= 16:
    print("Поздравляем вы поступили в ВГУИТ") 
else:
    print("Сначала нужно окончить школу!")
    s=16-age
    print("Осталось учиться", s ,"года(лет)")