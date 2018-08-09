 
x = input('Enter the numbers into the array with spaces between: ')
l=list(map(int,x.split(' ')))
print(l)
x=len(l)
for i in range(x-1):
    for j in range(1,x-i):
        if l[j-1]>l[j]:
            k=l[j]
            l[j]=l[j-1]
            l[j-1]=k
print(l)
