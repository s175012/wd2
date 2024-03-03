import sys

# a = 56
# print(a)
# print(type(a))
# b = 5.5
# print(b)
# print(type(b))
# zmienna_tekstowa = 'wizualizacja danych'
# print(zmienna_tekstowa)

# print(type(zmienna_tekstowa))

# a = 6
# b = 3

# c = a + b
# print(c)
# d = a-b
# print(d)
# e = 4
# f = b//a
# print(f)
# f = a//b
# print(f)
# g = a**2
# print(g)
# h = pow(a, 2)
# print(h)

# i = 6 ** (1/2)
# j = pow(6, 1/2)
# print(i)
# print(j)

# k = 'wizualizacja danych'
# l = ' grupa '
# m = 1
# print(k + l + str(m))
# print('liczba a jest rowna {:.2f}, liczba b jest rowna {}'
#      .format(*args:a, b)) # needs package args

# a = input('Wprowadz liczbe: ')
# print(a)
# print(type(a))
# a = int(a)
# print(a*5)
# print(type(a))

# sys.stdout.write('Wprowadz liczbe: ')
# b = sys.stdin.readline() # daje extra znak nowego wiersza
# print(b)
# print(type(b))

# lista = [5, 6.6, 34, 'a', 'b', [2, 3, 4], 'ab']
# print(lista)
# lista.append(67)
# print(lista)
# lista.insert(__index:2, __object:'c') # : zamiast =
# print(lista)
# lista.extend([20, 21, 22])
# print(lista)
# lista.pop()
# print(lista)
# lista.pop(2)
# print(lista)
# lista.remove([2, 3, 4])
# print(lista)
# del lista[1]
# print(lista)
# del lista doesn't work
# lista.reverse()
# print(lista)
# lista.sort() sorts numbers only lists
# print(lista)

# slownik = {'klucz': 'wartosc', 1: 2, 'a': 5, 4: 'b'}
# print(slownik)
# print(slownik[4])
# slownik[6] = 45
# print(slownik)
# slownik.pop(1)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# del slownik[6]

# a = 8
# b = 8
#
# if a > b:
#     print('a is greater than b')
# elif a < b:
#     print('a is less than b')
# else:
#     print('a is equal to b')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if (a > b) & (c >d):# or |
#     print(a, c)
# else:
#     print(b, d)

# for i in range(2, 8, 2):  # 1 arg to wartosc koncowa, 2 arg + w. startowa
#     print(i)  # 3 arg + w. skoku
# else:
#     print('koniec petli')

# for i in lista:
#     print(i)

# for i in range(0, 5):
#     for j in range(0, 5):
#         result = i+j
#         print(result)
#     print('')

# licznik = 0
# while licznik < len(lista):
#     print(lista[licznik])
#     licznik += 1
# else:
#     print('koniec petli')

# licznik = 0
# while licznik != 10:
#     if licznik == 7:
#         print(licznik)
#         break
#     else:
#         licznik += 1
# else:
#     print('licznik')

lista = [1, 2, 3, 4]
sys.stdout.write('Wprowadz liczbe: ')
li = int(sys.stdin.readline())
i = 0
while i<len(lista):
    if li-lista(i) == 0
          print(i, lista[i])
          break
    else:
          i+=1
else:
    print('nie ma takiej liczby')

# zrobic zadania