'''  list=[1,2,3,4,5,6,2,7,3,8,10,2]
unique1 = []
repeating=[]
def remove_duplicates(input_list):
    
    for i in input_list:
        if i not in  unique1:
            unique1.append(i)
        else: 
            if i not in repeating:
               repeating.append(i)
remove_duplicates(list)
print(unique1)
print(repeating)'''

lst=[2,3,4,5,4,2,3,3,3]
dict1={}
for i in lst:
    if lst.count(i)>1:
        dict1[i]=lst.count(i)
 