import random

MAX_ATTEMPTS = 10

#Генерируем случайное число
number = random.randint(1, 100)
attempts = MAX_ATTEMPTS

#Приветственное сообщение
print("Я загадал число от 1 до 100. У тебя 10 попыток.")

while attempts > 0:
    try:
        guess = int(input(f"Введите число ({attempts} попыток): "))
        attempts -= 1

    
        if guess < number:
            print("Загадочное число больше!")
        elif guess > number:
            print("Загадочное число меньше!")
        else:
            print(f"Да,точно в цель! Это было число {number}")
            print(f"Количество потраченных попыток {attempts}")
            break
    except ValueError:
            print("Пожалуйста, введите число!")
            continue

if attempts == 0:
    print(f"Попытки закончились. Загаданное число: {number}")
