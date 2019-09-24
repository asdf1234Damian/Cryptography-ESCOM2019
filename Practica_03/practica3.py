#I just want to let everyone know that i did this in like an hour with only 3 hrs of sleep and 
#  a whole night filles with self loathing. but it does what I was asked. 
import math
if __name__ == "__main__":
    n = int(input('Value for n: '))
    a = int(input('Value for α: '))

    a2,  n2 = a,n 
    if a>n :
        a,n = n,a
    while math.gcd(n, a) != 1:
        print('Invalid input, change α')
        a = int(input('Value for α: '))
    res = n%a
    
    eq1 = []
    eq2 = []
    while res!= 0:
        eq1.append(str(n).rjust(4) + ' = ' + str(a).rjust(4) + ('(' + str(n//a) + ')').ljust(4) +' + '+str((n%a)).rjust(3))
        eq2.append(str((n % a)).rjust(4) + ' = ' + str(n).rjust(4) + ' - ' + str(a).rjust(4) + '(' +str(n//a)+')')
        n,a= a,res
        res = n%a
    result = {}
    equations = []
    def egcd(a, b):
        global equations
        if a == 0:
            return (b, 0, 1)
        else:
            gcd, x, y = egcd(b % a, a)
            equations.append((x, y, a, b))
            return (gcd, y - (b//a) * x, x)
    
    temp = egcd(a2, n2)
    equations.append((temp[1],temp[2],0,0))
    print('1.- Se calcula el GCD ')
    for i in eq1:
        print(i)
    print('-'*50)
    print('2.- Transformar')
    for i in eq2:
        print(i)
    print('-'*50)
    print('3.- Sustitucion')
    for i in range(1,len(equations)-1):
        print('1 = '+str(equations[i][3])+'('+str(equations[i+1][1])+') + '+str(equations[i][2])+'('+str(equations[i+1][0])+')')
    print('-'*50)
    print('4.- Se calcula el resultado')
    print('α   :', equations[-2][2])
    print('α^-1:', equations[-1][0] % equations[-2][3])
