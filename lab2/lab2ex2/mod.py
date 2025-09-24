import random

def guessing_game(low: int = 1, high: int = 100) -> None:
    # комп'ютер загадує число. користувач відгадує, поки не вгадає.
    secret = random.randint(low, high)
    print(f"Я загадав число від {low} до {high}. Спробуйте відгадати!")
    attempts = 0
    while True:
        try:
            g = int(input("Ваш варіант: "))
        except ValueError:
            print("Введіть, будь ласка, ціле число.")
            continue
        attempts += 1
        if g < secret:
            print("Моє число більше.")
        elif g > secret:
            print("Моє число менше.")
        else:
            print(f"Ви вгадали! Кількість спроб: {attempts}")
            break
