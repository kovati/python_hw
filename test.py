szoveg = "valami"
# new = list(szoveg)
# new[2] = "f"
# print("".join(new))
ujszoveg = ''
for i in reversed(range(len(szoveg))):
    #print(szoveg[i])
    ujszoveg = ujszoveg + szoveg[i]
print(ujszoveg)
import math
print(math.log2(16))
valami = {24,45,33}
print(type(valami))
print(valami.union({23,45,78,89}))
valami = {24:34,45:56,67:78}
print(type(valami))
print(valami.keys())
valami = [1234,1234,1234]
print(type(valami))
print(valami[2])
valami = (1,2,3,4,6)
print(type(valami))
print(valami[2])
