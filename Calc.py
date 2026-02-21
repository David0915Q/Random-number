N1 = float(input("Первая цифра: "))
R = int(input("Знак (/, *, +, -) "))
N2 = float(input("Вторая цифра: "))

if R == 1:
    V = N1 / N2
elif R == 2:
    V = N1 * N2
elif R == 3:
    V = N1 + N2
elif R == 4:
    V = N1 - N2

print(V)


