# 1. Készítsünk programot, mely bekér két számot, majd kiírja az összegüket, a különbségüket, a
# szorzatukat és a hányadosukat. Az adatokat a billentyűzetről olvassuk be. A beolvasást
# mindaddig végezzük, míg helyes adatokat nem kapunk.

# isNumber = True
# while(isNumber):
#     ketszamsztring = input("Addj meg ket szamot, szokozzel elvalasztva\t")
#     szamlist = ketszamsztring.split(' ')
#     try:
#         tmp0 = int(szamlist[0])
#         print('The variable', szamlist[0], 'a number')
#         try:
#             tmp1 = int(szamlist[1])
#             print('The variable', szamlist[1], 'a number')
#             if isinstance(szamlist[0], str):
#                 print(type(szamlist[0]))
#             osszege = int(szamlist[0]) + int(szamlist[1])
#             kulonbsege = int(szamlist[0]) - int(szamlist[1])
#             szorzata = int(szamlist[0]) * int(szamlist[1])
#             hanyadosa = int(szamlist[0]) / int(szamlist[1])
#             print(f"A ket szam osszege:", osszege, f"A ket szam kulonbsege:", kulonbsege, f"A ket szam szorzata:",
#                   szorzata, f"A ket szam hanyadosa:", hanyadosa, )
#         except:
#             print('The variable', szamlist[1], 'is not a number')
#     except:
#         print('The variable', szamlist[0], 'is not a number')

# 2. Olvassunk be a billentyűzetről egy számot, majd írjuk ki a szám kétszeresét a képernyőre. A
# beolvasott számot és az eredményt nem kell mindenképpen tárolni.

# print(int(input("Addj meg egy szamot\t")) * 2)

# 3. Készítsünk konzol programot, amely bekér három egész számot a
# billentyűzetről. A bekért számokra úgy tekintünk, mint egy háromszög
# oldalaira. Döntsük el, hogy a háromszög szerkeszthető-e.
# Magyarázat: A háromszög abban az esetben szerkeszthető, ha bármely két oldal
# hosszának az összege nagyobb a harmadik oldal hosszánál.

# haromszamsztring = input("Addj meg harom szamot, szokozzel elvalasztva\t")
# szamlist = haromszamsztring.split(' ')
# try:
#     tmp0 = int(szamlist[0])
#     print('The variable', szamlist[0], 'a number')
#     try:
#         tmp1 = int(szamlist[1])
#         print('The variable', szamlist[1], 'a number')
#         try:
#             tmp2 = int(szamlist[2])
#             print('The variable', szamlist[2], 'a number')
#
#             szerkesztheto = (int(szamlist[0]) + int(szamlist[1])) > int(szamlist[2])
#             print(f"Szerkesztheto a haromszog?:", szerkesztheto )
#         except:
#             print('The variable', szamlist[2], 'is not a number')
#     except:
#         print('The variable', szamlist[1], 'is not a number')
# except:
#     print('The variable', szamlist[0], 'is not a number')

# 4. Készítsünk konzol programot, amely bekér három egész számot a billentyűzetről. A bekért
# számokra úgy tekintünk, mint egy háromszög oldalaira. Döntsük el, hogy a háromszög
# egyenlő oldalú, illetve egyenlő szárú háromszög‐e.

# haromszamsztring = input("Addj meg harom szamot, szokozzel elvalasztva\t")
# szamlist3 = haromszamsztring.split(' ')
# try:
#     first = int(szamlist3[0])
#     print('The variable', szamlist3[0], 'a number')
#     try:
#         second = int(szamlist3[1])
#         print('The variable', szamlist3[1], 'a number')
#         try:
#             third = int(szamlist3[2])
#             print('The variable', szamlist3[2], 'a number')
#             egyenlo_oldalu = (first == second) & (first == third)
#
#             egyenlo_szaru = (first == second) | (first == third) | (second == third)
#
#             print(f"Egyenlo oldalu a haromszog?:", egyenlo_oldalu , f"Egyenlo szaru a haromszog?:", egyenlo_szaru)
#         except:
#             print('The variable', szamlist[2], 'is not a number')
#     except:
#         print('The variable', szamlist[1], 'is not a number')
# except:
#     print('The variable', szamlist[0], 'is not a number')

# 5. Készítsünk konzol programot, amely bekér három egész számot a billentyűzetről. A
# bekért számokra úgy tekintünk, mint egy háromszög oldalaira. Számítsuk ki a
# háromszög kerületét.
# Magyarázat: A kerület kiszámítása nem okoz különösebb problémát, mivel egyenlő
# az oldalak hosszának az összegével. Amennyiben helyes programot szeretnénk
# készíteni figyeljünk arra is, hogy a háromszög szerkeszthető-e.
def valid_numbers(list):
    ret = False
    szamlist3 = haromszamsztring.split(' ')
    try:
        first = int(szamlist3[0])
        #print('The variable', szamlist3[0], 'a number')
        try:
            second = int(szamlist3[1])
            #print('The variable', szamlist3[1], 'a number')
            try:
                third = int(szamlist3[2])
                #print('The variable', szamlist3[2], 'a number')

                ret = [first, second, third]
            except:
                #print('The variable', szamlist[2], 'is not a number')
                ret = False
        except:
            #print('The variable', szamlist[1], 'is not a number')
            ret = False
    except:
        #print('The variable', szamlist[0], 'is not a number')
        ret = False
    return ret
# haromszamsztring = input("Addj meg harom szamot, szokozzel elvalasztva\t")
# haromint = valid_numbers(haromszamsztring)
# if haromint != False:
#     szerkesztheto = (haromint[0] + haromint[1]) > haromint[2]
#     if szerkesztheto:
#         print(f"Kerulete:", (haromint[0] + haromint[1] + haromint[2]))
#     else:
#         print("Nem szerkeszthato!")

# 6. Készítsünk konzol programot, amely bekér három egész számot a
# billentyűzetről. A bekért számokra úgy tekintünk, mint egy háromszög
# oldalaira. Számítsuk ki a háromszög területét. A terület kiszámításához
# használhatjuk a Hérón képletet.
# Magyarázat: A Hérón képlet segítségével a háromszög területét az oldalak hosszából
# is ki tudjuk számolni
# Az a, b és c a háromszög oldalai a képlettel számolhatók ki, ahol S a
# háromszög kerületének a fele

# haromszamsztring = input("Addj meg harom szamot, szokozzel elvalasztva\t")
# haromint = valid_numbers(haromszamsztring)
# if haromint != False:
#     szerkesztheto = (haromint[0] + haromint[1]) > haromint[2]
#     if szerkesztheto:
#         kerulet = haromint[0] + haromint[1] + haromint[2]
#         print(f"Kerulete:", kerulet)
#         s = kerulet / 2
#         terulet = (s * (kerulet - haromint[0]) * (kerulet - haromint[1]) * (kerulet - haromint[2])) ** 0.5
#         print(f"Terulete:", terulet)
#     else:
#         print("Nem szerkeszthato!")

# 7. Készítsünk olyan konzolos alkalmazást, amely beolvassa egy számtani sorozat első elemét,
# valamint a differenciáját, és egy tetszőleges N értéket, majd kiírja a sorozat elemét, és az
# első N tagja összegét.

# first_string = input("add meg az elso elemet\t")
# first = int(first_string)
# diff_string = input("add meg a differenciat\t")
# diff = int(diff_string)
# n_string = input("add meg az N-et\t")
# n = int(n_string)
# list = []
# new = first
# for i in range(0, n):
#     list.append(new)
#     new += diff
# print(list)
# osszeg = 0
# for szam in list:
#     osszeg += szam
# print(osszeg)

# 8. Készítsünk alkalmazást, amely beolvassa egy személy életkorát ( ), majd a kapott
# adat fényében kiírja a képernyőre azt a korosztályt, amibe az életkor „tulajdonosa”
# tartozik.
#  Gyermek (0-6),
#  Iskolás (7-22),
#  Felnőtt (22-64),
#  65 töl nyugdíjas!
age_string = input("add meg az eletkort\t")
age = int(age_string)
match(age):
    case age if age in range(0,6):
        print("Gyerek")
    case age if age in  range(7,22):
        print("Iskolás")
    case age if age in  range(23,64):
        print("Felnőtt")
    case age if age >=65:
        print("Nyugdíjas")
    case _:
        print("hibas eletkor")
