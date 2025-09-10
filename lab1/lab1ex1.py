# введення a
a = int(input("Введіть a: "))
while a <= 0:
    print("Помилка: a має бути додатним числом")
    a = int(input("Введіть a: "))

# введення b
b = int(input("Введіть b: "))
while b <= 0:
    print("Помилка: b має бути додатним числом")
    b = int(input("Введіть b: "))

# обчислення X
if a > b:
    x = a * b + 1
elif a == b:
    x = 25
else:
    x = (a - 5) / b

print("X =", x)
