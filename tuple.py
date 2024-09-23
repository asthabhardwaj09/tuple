# tuple data structure
# tuple can store any data type
# most important tuples are immutable, once tuple is created you cannot update
# data inside tuple
example=('one','two','three')
# no append , no insert , no pop , no remove
day=('monday','tuesday')
print(day)
# tuple are faster than list

# methods
# count,index
# len function
# slicing  eg. print(example[0])
# example[0]=1 
print(example)

''''''''''''''''''''''''''''''''''''''''''''''''

mixed=(1,2,3,4,0)

#for loop and tuple
for i in mixed:
    print(i)
  
#while loop and tuple  
i=0
while i<len(mixed):
    print(mixed[i])
    i+=1
    
#tuple with one element
# num=(1)
num=(1,)
print(type(num))

# words=('apple')
words=('apple',)
print(type(words))

#tuple without parenthesis

apple='apple','mango','grapes','gauva'
print(apple)
print(type(apple))

#tuple unpacking

cricketer=('dhoni','virat kholi','rohit sharma','shubham gill')
cricket1,cricket2,cricket3,cricket4=(cricketer)
print(cricket1)

cricketer = ('dhoni', 'virat kholi', 'rohit sharma', 'shubham gill')
cricket1,*remaining = cricketer
print(cricket1)

#list inside tuples

favorites=('sports',['music','food'])
favorites[1].pop()
favorites[1].append('travelling')
print(favorites)

#function we can used in tuples

#min(),max(),sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))

''''''''''''''''''''''''''''''''''''
# function returning two value

def fun(num1,num2):
    add=num1+num2
    multiply=num1*num2
    return add,multiply

# print(fun(2,3)) #gives value in tuple
add,multiply=fun(2,3)
print(add)
print(multiply)

''''''''''''''''''''''''''''''''''''
#something more about tuple, list,str

num=tuple(range(1,21))
print(num)

num=list((1,2,3,4,5,6,7,8))
print(num)
print(type(num))

num=str((1,2,3,4,5,6,7))
print(num)
print(type(num))

num_list=str([1,2,3])
print(num_list)
print(type(num_list))

