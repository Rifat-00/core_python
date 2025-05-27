#take name as input and print a greeting
user_name = input("Enter your user name: ")
print("Hello, "+user_name)

#take two number as input and print the sum
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
print("Sum of two number: ",(first_number+second_number))

#calculate the area of a rectangle
width = float(input("Enter the rectangle width: "))
height = float(input("Enter the rectangle height: "))
print("The are of rectangle: ",(width * height))


#take temperature in celsius and convert it to ferenhiehgt
celsius = float(input("Enter celsius: "))
to_ferenhiehgt = (celsius * 9/5)+32
print("In Ferenhiehgt:",to_ferenhiehgt)

#take input a number, and check if its positive, negative or zero
number = int(input("Enter your number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("its zero")


#check odd or even
number = int(input("Enter your number: "))
if number % 2 ==0:
    print("even")
else:
    print("odd")

#take age as input and check if they're eligible to vote
age = int(input("Enter your age: "))
if age > 18:
    print("You can vote")
else:
    print("Try after 18")

#take 3 numbers as input and print the largest one
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a>b and a>c :
    print("biggest:", a)
elif b>a and b>c:
    print("biggest: ",b)
else:
    print("biggest: ",c)

#simulate simple login, email and password
test_email = "admin@gmail.com"
test_pass = "123abc"
email = input("Enter your email: ")
password = input("Enter your password: ")
if email == test_email and password == test_pass:
    print("Access Granted")
else:
    print("Unauthorized")


#simple grade evaluation system
numbers = int(input("Enter your number: "))
if numbers >=90:
    print("A")
elif numbers >= 80 and numbers <90:
    print("B")
elif numbers >= 70 and numbers <80:
    print("C")
elif numbers >= 60 and numbers < 70:
    print("D")
else:
    print("Failed")

#print 1 - 10 using range
for i in range(1,11):
    print(i)

#print even number within 1-20
for i in range(1,21):
    if i%2==0:
        print(i)

#print sum of 1 to N
N = int(input("Enter your number: "))
sum = 0
for i in range(1,N+1):
    sum+=i
print(sum)

#print multiplication table for given number (upto 10)
n = int(input("Enter your number: "))
for i in range(1,11):
    print(f'{n}*{i} =',i*n)

#take number input until user types done and print the sum
total_sum = 0
print("""
      Enter all the necessary numbers.
      Type "done" when you are finished.
      """)
while True:
    user_input = input("Enter your number:")
    if user_input == "done":
        break
    numbers = int(user_input)
    total_sum+=numbers
print("Sum of your number: ",total_sum)

#print a square
size = int(input("Enter square size: "))
char_to_print = "*"
for i in range(size):
    print(char_to_print * size)

#find factorial of a given number
n = int(input("Enter your number: "))
fact = 1
for i in  range(n,0,-1):
    fact*=i
print(f'Factorial of {n}: ',fact)

#print all divisor
n = int(input("Enter your number: "))
for i in range(1,n+1):
    if n%i ==0:
        print(i)

#find prime number
n = int(input("Enter your number: "))
divisor_count = 0
for i in range(1,n+1):
    if n%i ==0:
        divisor_count+=1
if divisor_count == 2:
    print("it's a prime number.")
else:
    print("it's not a prime number.")

#take number as input and prints its digits
n = int(input("Enter your number: "))
temp_n = n 
while temp_n > 0:
    digit = temp_n % 10      
    print(digit)             
    temp_n = temp_n // 10    
    

#print 1-50 except multiples of 5
for i in range(1,51):
    if i % 5 ==0:
        continue
    print(i)

        

