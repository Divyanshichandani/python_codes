
#wap to create a list which takes numbers from 1 to 100 and siplays those numbers as even or odd
list_4 = [i for i in range(101)]
for i in list_4:
  if i%2 == 0:
    print(f'{i} is even')
  else:
    print(f'{i} is odd')


my_list = ["a", "1", "b", "2", "3", "4", "c", "d"]
result = [val for val in my_list if val.isdigit()]
print(result)
result2 = [val for val in my_list if val.isalpha()]
print(result2)


str_num = [1,'one',2,'two',3,'three',4,'four',5,'five',6,'six',7,'seven']
result = [str(i) for i in  str_num if str(i).isdigit()]
print(result)
result2 = [str(i) for i in str_num if str(i).isalpha()]
print(result2)


#wap to find the largest no. in a list which consist number 1 to 100
list = [10,33,53,32]
largest_number = list[0]

for num in list:
    if num > largest_number:
     largest_number = num

print("The largest number in the list is:", largest_number)