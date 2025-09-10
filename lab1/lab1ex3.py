N = int(input("Введіть N (1 < N < 9): "))
while N <= 1 or N >= 9:
    print("Помилка: N має бути від 2 до 8.")
    N = int(input("Введіть N (1 < N < 9): "))

# друк рядків
for i in range(N, 0, -1):
    line = ""
    for num in range(i, N + 1):
        line += str(num)
    print(line)
