def func_1(name): #def is used to define a function, also put the name of it,name is parameter.
    print(f'welcome to python {name}')
    print('python is a multipurpose programming language')

print('start the python') #outside the function
func_1('divs') #divs is an argument.if two arguments are passed under one parameter it will show error.
print('you can do anything in datascience using python')

#now using two parameters and two arguments.
def func_2(f_name,l_name):
    print(f'welcome {f_name} {l_name}')
func_2('DIVYANSHI','CHANDANI')

#cost and blah blah
def cost_1(mrp, shipping, discount):
    selling_price=mrp+shipping-discount
    print(selling_price)
print('total selling price')
cost_1(mrp=5000, discount=100, shipping=200) #this is keyword argument. we are deliberately assigning values to our arguments.if not specified it takes the values on its own respectively.


#wap to crerate a function that does arithmatic addition,subtraction,multiplication and division operation.take two operands.
def ari_operations(a,b):
  print('a+b=',a+b)
  print('a-b=',a-b)
  print('a*b=',a*b)
  print('a/b=',a/b)

ari_operations(10,5)


#wap in python to reverse a string.
s=input("Enter string: ")
"""print(s[::-1])"""
a=""
for i in s:
    a=i+a
print(a)


    
