# merge and extend the list

list1=["first","Second","Third"]
list2=[1,2,3]
print(list1)
print(list2)
list1.extend(list2)
print(list1)
list1.remove("first")
print(list1)

# sort list

number=[1,2,3,8,9,8]
number.sort(reverse=True)
print(number)
print(len(number))


# copy list

copynumber=number
print(copynumber)

# join list
num_list1=["a","b","c"]
num_list2=[1,2,3]
num_list3=num_list1+num_list2
print(num_list3)