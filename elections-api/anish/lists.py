l1 = [10, 34, 13, 23, 3, 10]
print(l1)
print('after appending')
# to add an element to the list
l1.append(5)

print(l1)

# how to duplicate the elements of a list
l1 = l1 * 2
print(l1)

# how to remove elements from a list
l1.remove(3) # removes the first occurrence of 3
print(l1)

l1.pop(3) # removes the element at index 3
print(l1)

l2 = [100, 200]
print(l2)
l3 = l1 + l2 # concatenation of two lists
print(l3)
