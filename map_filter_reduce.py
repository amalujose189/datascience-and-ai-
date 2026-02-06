'''from functools import reduce


list1=[1,2,3,4,5,6,7,8,9,10]
mapped_list=list(map(lambda x:x*2,list1)) #map function to double each element-modied value of list returned
filtered_list=list(filter(lambda x:x%2==0,list1))#filter function to get even numbers-only those elements returned which satisfy condition
reduced_value=reduce(lambda x,y:x+y,list1)#reduce function to get sum of all elements-reduce the list to a single value by applying a binary function cumulatively to the items of the list
print("Mapped List:",mapped_list)   
print("Filtered List:",filtered_list)
print("Reduced Value:",reduced_value)'''

'''def lastelement(lst):
    for i in lst:  #this is wrong because it will return the last element of the list not the last letter of each string in the list
        return i[-1] #The issue is that your lastelement function is designed incorrectly for use with map.
        break'''

'''When map(lastelement, list1) runs:

It passes "apple" (a single string) to the function
The loop iterates: i = 'a' (first character)
It immediately returns i[-1] which is 'a'[-1] = 'a' (first character!)
'''
list1=["apple","banana","cherry"]
def lastelement(item):
    return item[-1]
mapped1=list(map(lastelement,list1))
print(mapped1)
print("-----------------------------------------------------------")

list1=["apple","banana","cherry"]
mapped=list(map(lambda x:x[-1],list1))
#last letter of each string in list1

print(mapped)