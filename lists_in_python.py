#1.write  a program to create a list of prime numbers till 100
divvv = []
for i in range(2, 100):

    # Assume number is prime until shown it is not.
    a = True
    for x in range(2, i):
        if i % x == 0:
            a = False

    if a:
        divvv.append(i)
print(divvv)

#2.wap to swap first and last element of the list.
div=[2,3,4,5,6,7,8,9]
print(div)
a=div[0]
b=div[-1]
div[0]=b
div[-1]=a
print(div)

#3.wap to remove duplicates from list and sort them in ascending order
l1=[5,2,2,2,3,4,3,5,4,2,3,6,7,5,6,7]
a=[]
for i in l1:
    if i not in a:
        a.append(i)
        a.sort()
print(l1)
print(a)

