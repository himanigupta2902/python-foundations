list_1 = [1,2,3,4,5]
list_2 = [1,'two',3,4.1,'five','6']
print(len(list_2))
print(list_1[0])
print(list_2[2:])
print(list_1[:3])
list_2[1]='TWO CAPS'
print(list_2)
list_1.append('seven')
print(list_1)
print('popped item is : {} '.format(list_2.pop()))
print(list_2)
list_3 = ['e','a','x','o','e']
list_4= [7,3,4,1,9]
list_3.sort()
print(list_3)
list_4.reverse()
print(list_4)
list_5 = [1,2,3,[9,8,7]]
print(list_5[3][1])  ## 8

stuff=list()
stuff.append("Book")
stuff.append("Cookie")
stuff.append("Apple")
stuff.sort()
print(stuff)

inStr="My Name is Himani"
splitStr=inStr.split()
print(splitStr)
for i in splitStr:
    print(i)


######Chatgpt mini exercises #######
fruits = ["Apple","Banana","Mango"]
for fruit in fruits:
    print(fruit)

cities = ["Delhi", "Mumbai", "Bangalore", "Chennai"]
print(len(cities))

largest=None
smallest=None
numbers = [10, 5, 20, 15]
for num in numbers:
    if largest is None or num > largest:
        largest=num
    if smallest is None or num<smallest:
        smallest=num
print(largest)
print(smallest)

numbers = [10, 20, 30, 40, 50]
total=0
count=0
for num in numbers:
    total=total+num
    count=count+1
print(total)
print(count)


numbers = [10, 15, 20, 7, 8]
count=0
for number in numbers:
    if number%2==0:
        count=count+1
print(count)

numbers = [5, 12, 8, 25, 3, 15]
for num in numbers:
    if num>10:
        print(num)

