import math
from mod import guessing_game

def expr_z(m: float, n: float) -> float:
    # обчислення z=(sqrt(2)-sqrt(3*n))/(2*m)
    if n < 0:
        raise ValueError("Помилка: n має бути >= 0 (для sqrt(3n)).")
    if 2 * m == 0:
        raise ValueError("Помилка: знаменник (2*m) не може дорівнювати нулю.")
    return (math.sqrt(2) - math.sqrt(3 * n)) / (2 * m)

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
