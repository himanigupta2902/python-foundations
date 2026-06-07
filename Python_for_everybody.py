
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
