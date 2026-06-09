'''
name = input("Enter your name :")
print("Hello",name)


hours = int(input("Enter hours : "))
rate = float(input("Enter rate :"))
pay = hours*rate
print("Your total pay is",pay)

#### Conditional #######

var = int(input("Enter a number between 1 to 100 "))
if (var <= 10 ):
    print(f"{var} is a small number")
elif (var > 10 and var <=75):
    print(f"{var} is a medium range number")
else :
    print(f"{var} is a large number")



try:
    hours = float(input("Please enter number of hours: "))
    rate = float(input("Please enter the rate: "))
    if hours <= 40:
        pay=hours*rate
    else:
        pay=((40*rate)+((hours-40)*(rate*1.5)))
    print("final pay is ",pay)
except:
    print("Please enter a numeric number")
'''

#######Functions##################
'''
def calculatePay(hours,rate):
    if hours<=40:
        pay=hours*rate
    else:
        pay=((40*rate)+((hours-40)*(rate*1.5)))
    return pay

hours=float(input("Enter the number of hours: "))
rate=float(input("Enter the rate: "))
pay=calculatePay(hours,rate)
print("final pay is : ",pay)


def add(a,b):
    sum=a+b
    print("Result is",sum)

def subtract(a,b):
    diff=a-b
    print("Result is",diff)

a=float(input("Enter 1st number :"))
b=float(input("Enter 2nd number :"))
op=input("Choose operation (Add/Subtract):")
if op=='Add':
    add(a,b)
elif op=='Subtract':
    subtract(a,b)
else:
    print("No Operation Chosen")
'''

#########Loops######################

for i in [5,4,3,2,1]:
    if(i==3):
        break
    print(i)

### finding largest number ######
largest=0
for i in [3,41,33,22,75,8,69]:
    if(i>largest):
        largest=i
print("Largest number in the array is :",largest)

######doint operations in loop######

count=0
for i in [3,41,33,22,75,8,69]:
    count=count+1
    print(count,i)

count=0
for i in [3,41,33,22,75,8,69]:
    count=count+i
print("Sum of array is",count)

count=0
count1=0
for i in [3,41,33,22,75,8,69]:
    count=count+i
    count1=count1+1

print("Average of the array is",count/count1)

#####Loop exercise###############
sum=0
count=0
while True:
        userInput=input("enter a number :")
        if userInput=='done':
            break
        try:
            userInput=int(userInput)
        except:
            print("Invalid number")
            continue
        sum=sum+userInput
        count=count+1
print(f"Sum is {sum} , count is {count},average is {sum/count}")

