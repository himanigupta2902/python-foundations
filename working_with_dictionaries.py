seasons = dict()
seasons['summer']=12
seasons['fall']=3
seasons['winter']=8
seasons['spring']=9
print(seasons)
print(seasons['fall'])

##########Occurrance code using dictionaries ###########
fruits = dict()
names = ['Apple','Mango','Banana','Kiwi','Orange','Mango','Banana']
for i in names:
    if i not in fruits:
        fruits[i]=1
    else:
        fruits[i]=fruits[i]+1
print(fruits)

########## Better way #############
fruits = dict()
names = ['Apple','Mango','Banana','Kiwi','Orange','Mango','Banana']
for i in names:
    fruits[i]=fruits.get(i,0)+1
print(fruits)

############## Counting words using dictionaries and finding commonly used words #####################
wordOccurance=dict()
paragraph = "Python is an interpreted, high-level, and general-purpose programming language. Its design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear,logical code for small and large-scale projects."
wordList = paragraph.split()
for word in wordList:
    wordOccurance[word]=wordOccurance.get(word,0)+1
print(wordOccurance)
commonWord=None
maxCount=None
for i,j in wordOccurance.items():
    if maxCount is None or j > maxCount:
        maxCount=j
        commonWord=i
print(commonWord,maxCount)


###########Definite Loops #####################
fruits = {'Apple':1,'Mango':2,'Banana':3,'Kiwi':4}
for key in fruits:
    print(key,fruits[key])

fruits = {'Apple':1,'Mango':2,'Banana':3,'Kiwi':4}
print(list(fruits)) # ['Apple', 'Mango', 'Banana', 'Kiwi']
print(list(fruits.keys())) # ['Apple', 'Mango', 'Banana', 'Kiwi']
print(list(fruits.values())) # [1, 2, 3, 4]
print(list(fruits.items())) # [('Apple', 1), ('Mango', 2), ('Banana', 3), ('Kiwi', 4)]
for i,j in fruits.items():
    print(i,j)

