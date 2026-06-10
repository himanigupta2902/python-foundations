#####Problem 1: Count the input numbers#########
'''
count=0
while True:
    num=input("Enter a number :")
    if num=='done':
        break
    try:
        num=int(num)
    except ValueError:
        print("Enter a valid number")
        continue
    count=count+1
print("Count = ",count)


####### Problem 2 - Find the largest number and smallest number###########
large=None
small = None
while True:
    num=input("Enter a number : ")
    if num=='done':
        break
    try:
        num=float(num)
    except ValueError:
        print("Enter a valid number")
        continue
    if large is None or num>large:
        large=num
    if small is None or num<small:
        small=num
print("Largest number is : ",large)
print("Smallest number is : ",small)


################## Problem 3 : Find sum, average , count ########

sum=0
count=0
while True:
    num=input("Enter a number : ")
    if num=='done':
        break
    try:
        num=float(num)
    except ValueError:
        print("Enter a valid number")
        continue
    sum=sum+num
    count=count+1
if count==0:
    print("No numbers entered")
else:
    print(f"Sum = {sum} , average = {sum/count} , count = {count}")

'''

#############Print largest and 2nd largest number ########################
largest=None
secondLargest=None
while True:
    userIn = input("enter a number : ")
    if userIn == 'done':
        break
    try:
        userIn = int(userIn)
    except ValueError:
        print("enter a valid number ")
        continue
    if largest is None:
        largest=userIn
    elif userIn<largest and secondLargest is None:
        secondLargest=userIn
    if userIn>largest:
        secondLargest=largest
        largest=userIn
    if secondLargest<userIn<largest:
        secondLargest=userIn
print("Largest number is",largest)
print("Second largest number is",secondLargest)




