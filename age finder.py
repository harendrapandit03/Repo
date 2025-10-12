from datetime import date
PR="find your age" # Changes made now
print(PR.upper().center(50,'#'))
dd=int(input("enter day"))
mm=int(input("enter month"))
yy=int(input("enter year"))
print("Your age is:")
x=date.today()
p=x.year
q=x.month
r=x.day
y=date(yy,mm,dd)
j=y.year
k=y.month
l=y.day
if q<k:
    a=p-j-1
    print(a,"YEAR")
elif(q==k):
    if(r<l):
        a=p-j-1
        print(a,"YEAR")
    elif(r>=l):
        a=p-j
        print(a,"YEAR")
else:
    a=p-j
    print(a,"YEAR")
if(q<k):
    if(r<l):
        b=12-(k-q)-1
        print(b,"MONTH")
    elif(r>=l):
        b=12-(k-q)
        print(b,"MONTH")
elif(q==k):
    if(r<l):
        b=12-(k-q)-1
        print(b,"MONTH")
    elif(r>=l):
        b=0
        print(b,"MONTH")
else:
    if(r<l):
        b=q-k-1
        print(b,"MONTH")
    elif(r>=l):
        b=q-k
        print(b,"MONTH")
if(q<k):
    if(r<l):
        if (p % 4 == 0):
            match q:
                case 1:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 2:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 3:
                    c = r + (29 - l)
                    print(c,"DAYS")
                case 4:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 5:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 6:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 7:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 8:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 9:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 10:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 11:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 12:
                    c = r + (30 - l)
                    print(c,"DAYS")
        elif (p % 4 != 0):
            match q:
                case 1:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 2:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 3:
                    c = r + (28 - l)
                    print(c,"DAYS")
                case 4:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 5:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 6:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 7:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 8:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 9:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 10:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 11:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 12:
                    c = r + (30 - l)
                    print(c,"DAYS")
    elif(r>=l):
        c=r-l
        print(c,"DAYS")
elif(q==k):
    if(r<l):
        if (p % 4 == 0):
            match k:
                case 1:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 2:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 3:
                    c = r + (29 - l)
                    print(c,"DAYS")
                case 4:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 5:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 6:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 7:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 8:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 9:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 10:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 11:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 12:
                    c = r + (30 - l)
                    print(c,"DAYS")
        if (p % 4 != 0):
            match k:
                case 1:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 2:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 3:
                    c = r + (28 - l)
                    print(c,"DAYS")
                case 4:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 5:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 6:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 7:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 8:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 9:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 10:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 11:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 12:
                    c = r + (30 - l)
                    print(c,"DAYS")
    elif(r>=l):
        c=r-l
        print(c,"DAYS")
else:
    if(r<l):
        if(p%4==0):
            match k:
                case 1:
                    c=r+(31-l)
                    print(c,"DAYS")
                case 2:
                    c=r+(29-l)
                    print(c,"DAYS")
                case 3:
                    c=r+(31-l)
                    print(c,"DAYS")
                case 4:
                    c=r+(30-l)
                    print(c,"DAYS")
                case 5:
                    c=r+(31-l)
                    print(c,"DAYS")
                case 6:
                    c=r+(30-l)
                    print(c,"DAYS")
                case 7:
                    c=r+(31-l)
                    print(c,"DAYS")
                case 8:
                    c=r+(31-l)
                    print(c,"DAYS")
                case 9:
                    c=r+(30-l)
                    print(c,"DAYS")
                case 10:
                    c=r+(31-l)
                    print(c,"DAYS")
                case 11:
                    c=r+(30-l)
                    print(c,"DAYS")
                case 12:
                    c=r+(31-l)
                    print(c,"DAYS")
        elif p % 4 != 0:
            match k:
                case 1:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 2:
                    c = r + (28 - l)
                    print(c,"DAYS")
                case 3:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 4:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 5:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 6:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 7:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 8:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 9:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 10:
                    c = r + (31 - l)
                    print(c,"DAYS")
                case 11:
                    c = r + (30 - l)
                    print(c,"DAYS")
                case 12:
                    c = r + (31 - l)
                    print(c,"DAYS")
    elif r>=l:
        c=r-l
        print(c,"DAYS")









