import random

# Минимальное и максимальное число для игры
min_number = 1
max_number = 100

# Количество ходов до поражения
number_to_lose = 7

# Ход бота 
bot_choice = random.randint(min_number, max_number)

# Объявление о игре 
print(f"Я загадал число от {min_number} до {max_number}. У тебя {number_to_lose} попыток что бы угадать.")


while True: 
    # Ход игрока
    user_choice = int(input("Ваш ход, впишите число: "))
    # Подсчет попыток -1
    number_to_lose -= 1

    # Проверка на правильность ввода
    if user_choice == bot_choice:
        print("Поздравляю вы угадали!")
        break
    elif user_choice < min_number or user_choice > max_number:
        print(f"Некорректный ввод! Введите число от {min_number} до {max_number}")
    elif user_choice < bot_choice:
        print(f"Загаданное число больше! Осталось попыток: {number_to_lose}")
    elif user_choice > bot_choice:
        print(f"Загаданное число меньше! Осталось попыток: {number_to_lose}")   
        
    # Проверка на конец игры
    if number_to_lose == 0:
        print(f"Вы проиграли! Загаданное число: {bot_choice}")
        break



