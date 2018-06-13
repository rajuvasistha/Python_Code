#!/usr/bin/env python3
from datetime import date
nm=[]
x=0
nm.append(date.today())
qa=str(nm[0])
#print(len(qa))
mp=1000
z=0
i=0
a=0
while z<4:
    a+=int(qa[i])*mp
    mp=mp//10
    z=z+1
    i=i+1
print(a)
#print(qa)
b=0
b=int(qa[5])*10+int(qa[6])
#print(b)
c=0
c=int(qa[8])*10+int(qa[9])
#print(c)

bd=int(input("Please Input Born Date :"))
bm=int(input("Please Input Born Month :"))
by=int(input("Please Input Born Year :"))
if(c<bd):
    cd+=30
    b-=1
if(b<bm):
    b+=12
    cy-=1
ry=rm=rd=0
ry=a-by
rm=b-bm
rd=c-bd
print("=================================")
print("Year :",ry,"Month ",rm,"Day :",rd)
print("=================================")






