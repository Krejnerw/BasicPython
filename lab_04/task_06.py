# Napisz skrypt, który pobiera od użytkownika wartość liczbową, a następnie wyświetla na konsoli zdanie w postaci: "Podaną liczbę można zapisać jako: ...", gdzie zapis będzie w postaci sumy iloczynów liczb dla każdego rzędu. Np. liczba 123: "Podaną liczbę można zapisać jako: 100 * 1 + 10 * 2 + 1 * 3". Do pobrania i wypisania wartości użyj odpowiednio instrukcji readline() i write() z modułu sys).

import sys

print("Enter a number: ")
number = int(sys.stdin.readline())
row = 1
response = []
while number != 0:
    tmp = number % 10
    number -= tmp
    text = f'{row} * {tmp}'
    response.append(text)
    if number != 0:
        response.append(" + ")
    number //= 10
    row *= 10
response.reverse()
sys.stdout.write("".join(response))
