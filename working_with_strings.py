print("hello")
print('hello World')
print("I'm a girl")
print('I read books \n Sapiens \n Song of Ice and Fire \n\t House of Dragons')
print(len('hello'))
print(len("i'm a girl"))

### String Slicing and Indexing ###

mystring="Hello World"
print(mystring)
print(mystring[0])
print(mystring[6])
print(mystring[-1])
print(mystring[-10])
print(mystring[3:])
print(mystring[:7])
print(mystring[3:7])
print(mystring[5:-1])
print(mystring[5:])
print(mystring[::2])
print((mystring[2:10:2]))
print(mystring[::-1])
print(mystring[10:2:-2])

###### string concatenation #######

mystring_1 = "It's a beautiful day"
print(mystring +'\t'+ mystring_1)
print(mystring + '\n' + mystring_1)
test = 'Sam'
print('P' + test[1:])
letter = 'z'
print(letter*10)

print(5+6)
print('5' + '6')
print(mystring.upper())
print((mystring.lower()))
print(mystring_1.split())
print(mystring_1.split('t'))

#### String format ######
print('This is a {}'.format('STRING'))
print('This {} a {}'.format('is','STRING'))
print('{q} {b} {f}'.format(q='quick',b='brown',f='fox'))
print('The result is {}'.format(100/33))
print('The result is {r:1.3f}'.format(r=100/33))
name = "Himani"
print(f'Hello ! My name is {name}')  # new way
name = "Tanuj"
age = 33
print(f"{name}'s age is {age}")