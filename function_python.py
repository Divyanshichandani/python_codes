def square(n):
  return n**2
def sum(a,b):
  square(a)  #a=square(a)
  return a+b

result=square
print(result(5))
summation=sum(10,7)
print(summation)

##global and local variable

num_1=100    #global: declared outside of a function
def summ():
  num_1=50   # local: declared inside a function
  print(num_1) #50
def summm():
  print(num_1) #100

summ()
summm()

list_1=[1,2,3,4,5,6,7,8]
def list_del():
  del list_1[0]
  return list_1
  
def list_append():
  list_1.append(90)
  return list_1
list_del()
print(list_1)
list_append()
print(list_1)

#wap that calculates the frequency of words in a sentence using functions
#a=this is a picture this is beautiful
def frequency(a):
  word=a.split()
  list_1=[]
  for i in word:
    if i not in list_1 :
      list_1.append(i)
  for i in range(0,len(list_1)):
      print('Frequency of' ,list_1[i], 'is',a.count(list_1[i]))


a="this is a picture this is beautiful"
print(frequency(a))

##wap to calculate the frequency of characters in a string
def count(str_1):
  freq = {}
  for i in str_1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
  print('Count of all characters in', str_1,' is :' + str(freq))

str_1='hello'
print(count(str_1))

    


 
  
