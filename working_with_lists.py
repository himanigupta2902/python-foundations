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