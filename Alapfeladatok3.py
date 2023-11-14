# 1 Átlag fölöttiek
# Kérjük be az osztály 10 tanulójának matematika érdemjegyeit. A számok alapján határozzuk
# meg az osztályátlagot, majd határozzuk meg hány diák jegye volt magasabb mint az átlag.
osztaly_matekjegyei = input("Addja meg az tanulok matekjegyeit szokozzel elvalasztva\t")
matek_jegyek_stringlist = osztaly_matekjegyei.split(' ')
tanulok_szama = len(matek_jegyek_stringlist)
osszeg = 0
for jegy in matek_jegyek_stringlist:
    osszeg += int(jegy)
print(f"A tanulok matekjegyeinek atlaga:", osszeg/tanulok_szama, f"es tanulok letszama:", tanulok_szama)

# 2 Különböző számok
# Kérjük be 5 db számot billentyűzetről, de csak különbözőeket fogadhatunk el. Amennyiben a
# bevitel során olyan számot írna be, amely már szerepelt volna, úgy figyelmeztessük, és ezen
# számot írja be újra (amíg az különböző nem lesz).
number_set = set()
i = 0
while(i < 5):
    entered_number = input("Adjon meg egy szamot")
    print(number_set.add(entered_number))
    print(number_set)
    if number_set.add(entered_number):
        print("Ezt a szamot mar megadta korabban! Kulonbozo szamot kell megadnia")
    else:
        i += 1
print(number_set)
# 3 Minimum és maximum
# Töltsünk fel 1..100 közötti véletlen számokkal egy 20 elemű vektort. Írjuk ki a vektor elemeit
# a képernyőre, majd határozzuk meg és írjuk ki a legkisebb és legnagyobb elem értékét is a
# képernyőre.
# 4 Van-e ismétlődés
# Töltsünk fel véletlenszámokkal egy vektorrt, és határozzuk meg, van-e benne olyan elem,
# amely ismétlődik, vagyis többször is szerepel.
# 5 Legtöbbet előforduló elem
# Kérjünk be (vagy töltsünk fel véletlenszámokkal) egy vektort 1..10 közötti számokkal, majd
# határozzuk meg melyik az az érték, amely legtöbbször szerepel a tömbben.
# 6 Magasságmérés
# 5 km-enként megmértük a felszín tengerszint feletti magasságát. (összesen N mérést
# végeztünk) A méréseket szárazföld felett kezdtük és fejeztük be. Ott van tenger, ahol a mérés
# eredménye 0 (víz), másutt nagyobb mint 0 (szárazföld). Határozzuk meg, van-e ezen a
# tengerszakaszon sziget!
# Lehetséges kiegészítések:
#  hány szigeten jártunk?
#  Adjuk meg azt a szigetet (kezdő index), ahol a legmagasabb csúcs van!
#  Írjuk ki a tengerszakaszok hosszát!
#  Állapítsuk meg hogy van-e két egyforma szélességű (hosszú) sziget!
# 7 Számrendszer átváltó
# Kérjünk be egy egész számot, és egy számrendszerbeli alapszámot (2..16). Írjuk ki az adott
# egész szám ezen számrendszerbeli alakját.
# 8 Nagyobbak
# Egy random feltöltésű tömbben határozzuk meg, hogy van-e olyan szám, amely mindkét
# szomszédjánál nagyobb.
# 9 Összegzés
# Egy 30 elemű vektort töltsünk fel véletlen értékekkel a 10,80) intervallumból. Írassuk ki az
# elemeket egymástól vesszővel elválasztva. Kérjünk be egy A és B számot, határozzuk meg
# hány vektorbeli elem szerepel az [A,B] intervallumból (pl. hány szám van a (30,50)
# intervallumból).