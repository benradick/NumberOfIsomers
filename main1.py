n=int(input('No Carbons'))
c=1
h=0
E=0
noofis=0
sum1=0

#adding a diffrent comments

#this is an edited version, but it is the same more or less

A=[]
for a in range(n):
    A.append([0])

if n==2:

    B=A

    for i in range(1,5):
        B[0]=i
        for j in range(c,5):
            B[1]=j
            print(B)
            h=h+1
            sum1=0
            for el in range(n):
                sum1=sum1+int(B[el])
            if int(sum1)==(2*n-2):
                print('VALID^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                noofis=noofis+1

        c=c+1

elif n==3:

    B=A

    for i in range(1,5):
        B[0]=i
        for j in range(c,5):
            B[1]=j
            k=1
            for k in range(j,5):
                B[2]=k
                print(B)
                h=h+1
                sum1=0
                for el in range(n):
                    sum1=sum1+int(B[el])
                if int(sum1)==(2*n-2):
                    print('VALID^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                    noofis=noofis+1

        c=c+1

elif n==4:

    B=A

    for i in range(1,5):
        B[0]=i
        for j in range(c,5):
            B[1]=j
            k=1
            for k in range(j,5):
                B[2]=k
                l=1
                for l in range(k,5):
                    B[3]=l
                    print(B)
                    h=h+1
                    sum1=0
                    for el in range(n):
                        sum1=sum1+int(B[el])
                    if int(sum1)==(2*n-2):
                        print('VALID^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                        noofis=noofis+1

        c=c+1

elif n==5:

    B=A

    for i in range(1,5):
        B[0]=i
        for j in range(c,5):
            B[1]=j
            k=1
            for k in range(j,5):
                B[2]=k
                l=1
                for l in range(k,5):
                    B[3]=l
                    t=1
                    for t in range(l,5):
                        B[4]=t
                        print(B)
                        h=h+1
                        sum1=0
                        for el in range(n):
                            sum1=sum1+int(B[el])
                        if int(sum1)==(2*n-2):
                            print('VALID^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

                            noofis=noofis+1

        c=c+1

elif n==9:

    B=A

    for i in range(1,5):
        B[0]=i
