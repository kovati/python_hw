# # 1. Írjon programot, mely kiírja a képernyőre az első tíz egész számot visszafelé!
# from xmlrpc.client import MAXINT
#
# print("1. Feladat:")
# for i in range(10):
#     print(9-i)
# # 2. Alakítsa át az előző programot úgy, hogy az csak a páros számokat írja a képernyőre!
# print("\n2. Feladat:")
# for i in range(10):
#     if (9-i) % 2 == 0:
#         print(9-i)
# # 3. Írassa ki a képernyőre az első n egész szám összegét!
# print("\n3a. Feladat:")
# n = int(input("Add meg az n-et:"))
# osszeg = 0
# for i in range(n):
#     osszeg += i
# print(osszeg)
# print("\n3b. Feladat:")
# osszeg2 = n * (n-1) / 2
# print(osszeg2)
# # 4. Írassa ki a képernyőre az első n egész négyzetszámot!
# print("\n4. Feladat:")
# n = int(input("Add meg az n-et:"))
# for i in range(n):
#     print(i*i)
# # 5. Írjon programot, mely beolvassa a billentyűzetről egy intervallum kezdő és
# #     végértékét, majd kiírja a képernyőre az intervallumba eső egész számok közül azokat,
# #     melyek 3-mal és 5-tel is oszthatók!
# print("\n5. Feladat:")
# start = int(input("Kezdo ertek:"))
# end = int(input("Vegertek:"))
# for i in range(start, end+1):
#     if (i % 3 == 0) | (i % 5 == 0):
#         print(i)
#
# # 6. Készítsen programot, mely beolvassa a billentyűzetről az egész számokat egy
# #     meghatározott végjelig. Az éppen beolvasott számnak írja ki a négyzetét.
# print("\n6. Feladat:")
# n = input("Adj meg egy egesz szamot vagy q-t a kilepeshez:")
# while n != 'q':
#     number = int(n)
#     print(number * number)
#     n = input("Adj meg egy egesz szamot vagy q-t a kilepeshez:")
# # 7. A felhasználótól beolvasott számot a program váltsa át kettes számrendszerbe!
# print("\n7. Feladat:")
# n = int(input("Adj meg egy egesz szamot a kettes számrendszerbe valtashoz:"))
# i = 0
# binary = "00000000"
# binary_list = list(binary)
#
# for i in reversed(range(8)):
#     # print("n:", n, " i:", i, " binary:", binary_list)
#     if (n - (2 ** i)) >= 0:
#         binary_list[7-i] = "1"
#         n = n - (2 ** i)
#     else:
#         binary_list[7-i] = "0"
# print("".join(binary_list))
# 8. Programja olvasson be a billentyűzetről egész számokat egy meghatározott végjelig
#     (legyen a végjel -999999), majd a végjel beolvasása után írja ki a legnagyobbat és a
#     legkisebbet a kapott értékek közül.

# 9. Írjon programot, mely kiírja az első n db páros szám összegét a képernyőre!
# print("\n9. Feladat:")
# n = int(input("Adj meg egy egesz szamot:"))
# osszeg = 0
# for i in range(1, n + 1):
#     print(i)
#     if i % 2 == 0:
#         osszeg = osszeg + i
# print(osszeg)
#
# print("\n9b. Feladat:")
# n = int(input("Adj meg egy egesz szamot:"))
# osszeg = 0
# count = 0
# i = 0
# while count < n:
#     # print("count", count, "i", i, "osszeg", osszeg)
#     if i % 2 == 0:
#         osszeg = osszeg + i
#         count = count + 1
#     i = i + 1
# print("az első", n, "db páros szám összege", osszeg)
# # 10. Készítsen programot, mely beolvas n db számot a billentyűzetről, majd meghatározza
# #     a számok átlagát.
# print("\n10. Feladat:")
# numbers = input("Adj meg egesz szamotokat, ha vege Enter:")
# number_list = numbers.split()
# sum = 0
# for i in range(0, len(number_list)):
#     print("i",i, "sum", sum, "i. elem", int(number_list[i]))
#     sum = sum + int(number_list[i])
# print("Average:", (sum / len(number_list)))
# 11. Készíts programot, amely (maximum 99 karakter hosszú) mondatokat kér be a
#     felhasználótól, és minden bekérés után kiírja, hogy a megadott mondat palindróma-e!
#     (A palindróma olyan mondat, ami előre és visszafelé olvasva ugyanaz.) A programnak
#     lehessen megadni szóközöket tartalmazó mondatot is! A palindróma-vizsgálatnál a
#     program ne vegye figyelembe a fehér karaktereket .A kis és a nagy betűk ne
#     számítsanak különbözőnek! Feltételezheted, hogy a mondatok nem tartalmaznak
#     ékezetes betűket és jeleket. Ha a felhasználó a "kilep" mondatot adta meg, akkor a
#     program lépjen ki!
#         Példa futási eredmény:
#             Sanyi, kek az eg.
#             Nem palindroma.
#             Geza, kek az eg.
#             Palindroma!
#             kilep
print("\n11. Feladat:")
sentence = input("Adj meg egy modatot, ha vege Enter:")
#sentence = sentence.replace(',', '').replace('.', '').replace(' ', '')
reverse_sentence = ""
#print(sentence.strip())
while sentence != "kilep":
    sentence = sentence.replace(',', '').replace('.', '').replace(' ', '')
    sentence = sentence.lower()
    for i in reversed(range(len(sentence))):
        #print(sentence[i])
        reverse_sentence = reverse_sentence + sentence[i]
    print(reverse_sentence)
    if sentence == reverse_sentence:
        print("Palindroma!")
    else:
        print("Nem palindroma.")
    sentence = input("Adj meg egy modatot, ha vege Enter:")
    reverse_sentence = ''