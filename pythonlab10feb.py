
#write a function to find factorial of a number

'''def factorial(a):
    if(a==0 or a==1):
        print(1)
    else:
        c=1
        for i in range (2,a+1):
            c*=i
        print(c)
        
a=int(input("Enter a: "))
factorial(a)


#waf for fibonacci series
def fibonacci(n):
    a=0
    b=1
    print(a,b)
    for c in range(1,n+1):
        c=a+b
        a=b
        b=c
        print(c)
fibonacci(7)

#waf to find if a number is prime and even

def primeeven(num):
    if (num%2==0 or num>1):
        for i in range(2,num):
            if(num%i==0):
                print(num,"is not a prime number")
            else:
                print(num,"is a prime number")
        print(num,"number is even")
    else:
        num==1
        
        print(num," is not a  prime")
    

num=int(input("enter the number"))
primeeven(num)'''

#lambda() function -used to define an anonymous function in python,used for single line functions
def recur_fibo(n):
  if n<=1:
     return n
  else:
    return (recur_fibo(n-1) + recur_fibo (n-2))
  nterms =10
  if nterms<=0:
    print (" enter the number ")
  else:
    print (" Fibonacci series ")
    for i in range(nterms):
      print(recur_fibo(i))


#wap for 
      
        

    


#recursion