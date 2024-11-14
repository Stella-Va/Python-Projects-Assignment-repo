#numbers = [0, 254, 2, -1, 3]

#for num in numbers:
  #if (num < 0):
    #print("Negative number detected!")
   # break
 # print(num)


  #continue keyword
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)