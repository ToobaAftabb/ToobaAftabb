

# Activity 1:

for i in range(20):
    if i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        print("Bingo !!")
        print("-----")
    else:
        pass



#  Activity 2:

n = input("Enter a Number: ")

if int(n) % 2 == 0:
    print("The Number  "+n+"  is Even Number")
else:
    print("The Number  "+n+"  is Odd Number")



#  Activity 3:

sum= 0
n = int(input("Enter Any Integer    :"))

while n !=0:
    n = int(input("Enter Any Integer    :"))
    sum=sum+n

print("Sum of the Integers Is    :", sum)


#   Activity 4:

isPrime = True
i = 2
n = int(input("Enter a Number   :"))
while i<n:
    rem = n%i
    if rem == 0:
        isPrime = False
        break
    else:
        i = i+1
if isPrime:
    print(n, " is a prime Number   ")
else:
    print(n, " is not a prime Number   ")




sum = 0
i = 1
while i<=5:
    s= int(input("Enter a  Number       :"))
    sum=sum+s
    i=i+1

print("Sum Of the Integers is  :", sum)


sum = 0
i =1
while i<=10:
    print(i)
    sum=sum+i
    i=i+1

print("--------")
print("Sum is ", sum)


num = int(input("Enter A Number      :"))

reversed = 0
while n != 0:
     digit = int(n % 10)
     reversed = int(reversed * 10 + digit)
     n=int(n/10)


print("Reversed Number is  :", reversed)



n= 1
while n!=0:
    n = int(input("Enter Number: "))
    if n%2==0:
        print("Even Number ")
    elif n%3==0:
        print("Odd Number ")
    else:
        print("-----")
        pass





inp = int(input("Enter a number to find  :"))
fact=1

while inp !=0:
    fact=fact*inp
    inp= inp-1

print("Factorial Of Number  is  ", fact )




n = int(input('Enter a marks of student:'))

if n>100:
    print('invalid input')
else:
    if n<50:
        print('You Grade is F',n)
    elif n>50 and n<60:
        print(' Your Grade is E, ,n)
    elif n>61 and n<70:
        print('Your Grade is D',n)
    elif n>71 and n<80:
        print('Your Grade is C',n)
    elif n>81 and n<90:
        print('Your Grade is B',n)
    elif n>91 and n<100:
        print('Your Grade is A',n)

