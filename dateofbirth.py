cd=0
cm=0
cy=0
bd=0
bm=0
by=0
rd=0
rm=0
ry=0
cd=int(input("INPUT CURRENT DATE :"))
cm=int(input("INPUT CURRENT MONTH :"))
cy=int(input("INPUT CURRENT YEAR :"))
bd=int(input("INPUT BORN DATE :"))
bm=int(input("INPUT BORN MONTH :"))
by=int(input("INPUT BORN YEAR:"))
if(cd<bd):
    cd+=30
    bm-=1
if(cm<bm):
    cm+=12
    cy-=1
rd=cd-bd
rm=cm-bm
ry=cy-by
print(ry,rm,rd)

