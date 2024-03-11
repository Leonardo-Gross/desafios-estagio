n = int(input("Insira um número para gerar uma sequência de Fibonnaci: "))

t1 = 0
t2 = 1
t3 = 0
list = []


print(f'{t1} - {t2}', end='')
while n > t3:   
    t3 = t1 + t2
    list.append(t1)
    list.append(t2)
    list.append(t3)
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    if n  == 0 or n == 1:
        print('\nO número faz parte da sequência de Fibonacci!')
    elif n == t3:
        print('\nO número faz parte da sequência de Fibonacci!')
if n not in list:
    print('\nO número não faz parte da sequência de Fibonacci!')
 
