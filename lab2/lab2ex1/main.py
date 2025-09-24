import math
import random

def expr_z(m: float, n: float) -> float:
    # обчислення z=(sqrt(2)-sqrt(3*n))/(2*m)
    if n < 0:
        raise ValueError("Помилка: n має бути >= 0 (для sqrt(3n)).")
    if 2 * m == 0:
        raise ValueError("Помилка: знаменник (2*m) не може дорівнювати нулю.")
    return (math.sqrt(2) - math.sqrt(3 * n)) / (2 * m)

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

if __name__ == "__main__":
    # обчислення виразу
    print("z=(sqrt(2)-sqrt(3*n))/(2*m)")
    try:
        n = float(input("Введіть значення n: "))
        m = float(input("Введіть значення m: "))
        z = expr_z(m, n)
        print("Значення виразу z =", z)
    except ValueError as e:
        print(e)

    # гра
    print("\nПочнемо гру 'Відгадай число'.")
    guessing_game()
