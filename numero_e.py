import os
def factorial(n:int) -> int:
    tot=n
    i=n-1
    if n==0:
        return 1
    while i != 0:
        tot *= n-i
        i-=1
    return tot

limit = 4
e = 0
for i in range(limit):
    e += 1/(factorial(i))
print("\n\n\nNumero e con precision",limit,"es: ", e,"\n\n")
os.system("pause")