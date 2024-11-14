#Create a function that determines whether or not a number is divisible by ten. 
# A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this,
#  we can complete this function in a few steps:

#Define the function header to accept one input num
#Calculate the remainder of the input divided by 10 (use modulus)
#Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False




#Coding question

#Create a function called divisible_by_ten() that has one parameter named num.

#The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

def divisible_by_10(num):

  if num % 10 == 0:    
    return True
  else:
    return False

print(divisible_by_10(180))
print(divisible_by_10(10))
print(divisible_by_10(567)) 
