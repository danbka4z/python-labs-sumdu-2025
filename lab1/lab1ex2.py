first = 30
last = 60

print("Числа, які кратні 3 у проміжку від 30 до 60:")
count = 0

for n in range(first, last + 1):
    if n % 3 == 0:
        print(n, end=" ")
        count += 1

print()
print("Кількість: ", count)
