a=0
b=0
i=0
x=[12,14,19,26]
y=[13,20,30,40]
z=[0,0,0,0,0,0,0,0]
for f in range(0,4):
    if(x[a]>y[b]):
        z[i]=x[a]
        a=a+1
        i=i+1
        print("Master work")
    else:
        z[i]=y[b]
        b=b+1
        i=i+1
print(z)
