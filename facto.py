def fact(a):
    fact=1
    i=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
x=int(input(" Please Input the value  "))
print(fact(x))





