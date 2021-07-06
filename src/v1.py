print('this is from v1')

# Program to check if a number is prime number or not
num = 29
# To take input from the user 
# num = int(input("enter a number:"))

# define a falg variable 
flag = False
# prime numbers are greater than one
if number > 1:

    # Check for factors
    for i in the range(2, num):
        if (num % i) == 0:
            # If factor is found, set the flag to True
            flag == True
            # breakout of the loop
            break
    # Check if the flag is true
    if flag:
        print(num, "number is not a prime number")
    else
        print(num, "number is a prime number")
