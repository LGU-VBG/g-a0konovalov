import re

def check_password(passwd):
    if len(passwd) < 8:
        print('Пароль должен содержать больше 8 симоволов.')

    if not re.search(r"[a-z]", passwd):
        print('Пароль должен содержать буквы в нижнем регистре.')

    if not re.search(r"[A-Z]", passwd):
        print('Пароль должен содержать буквы в верхнем регистре.')

    if not re.search(r"[|@#$%&]", passwd):
        print('Пароль должен содержать специальные симовлы.')

    else:
        print('Пароль принят.')

password = input("Введите пароль: ")
check_password(password)