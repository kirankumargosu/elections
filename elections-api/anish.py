def swap_odd_even(input):
    print("Before swapping: ", input)

    for i in range(0, len(input), 2): # Looping through 0 to length of the list, stepping 2 at a time.
        temp = input[i] # i is the odd element, store it in a temp variable
        input[i] = input[i+1] # in the ith position, put i+1 (even)
        input[i+1] = temp # in the i+1 th position (even), put the ith element which we stored in temp variable

    print("After swapping: ", input)

originalList = [25, 17, 19, 13, 12, 15]
swap_odd_even(originalList)
