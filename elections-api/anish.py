def swap_odd_even(input):
    print("Before swapping: ", input)

    for i in range(0, len(input), 2): # Looping through 0 to length of the list, stepping 2 at a time.
        temp = input[i] # i is the odd element, store it in a temp variable
        input[i] = input[i+1] # in the ith position, put i+1 (even)
        input[i+1] = temp # in the i+1 th position (even), put the ith element which we stored in temp variable

    print("After swapping: ", input)

originalList = [25, 17, 19, 13, 12, 15]
# swap_odd_even(originalList)

def read_simple_file_full():
    print("********* read_simple_file_full - start")
    f = open("simple.txt", "r")
    all_data = f.read()
    print(type(all_data))
    print(all_data)
    f.close()
    print("******** read_simple_file_full - end")

def read_simple_file_line_by_line():
    print("********* read_simple_file_line_by_line - start")
    f = open("simple.txt", "r")
    lines = f.readlines()
    print(type(lines))
    for line in lines:
        print(line, end="")
    f.close()
    print("\n********* read_simple_file_line_by_line - end")

# read_simple_file_full()
# read_simple_file_line_by_line()


import csv
def read_csv_file():
    print("********* read_csv_file - start")

    print("Reading csv as a whole - start")
    f_full_data = open("commsepval.csv", "r")
    data = f_full_data.read()
    print("Type of data is ", type(data)) # str
    print(data)
    f_full_data.close()
    print("Reading csv as a whole - end")
    
    
    print("Reading csv line by line - start")
    hasHeader = True
    f_line_by_line = open("commsepval.csv", "r")
    lines = f_line_by_line.readlines()
    print("Type of lines is ", type(lines))  # list
    for line in lines:
        print("Type of line is ", type(line)) # str
        print(line)
    f_line_by_line.close()
    print("Reading csv line by line - end")

    print("Reading csv using csv module - start")
    f_csv = open("commsepval.csv", "r")

    csvreader = csv.reader(f_csv)
    if hasHeader == True:
        header = next(csvreader)
        print("Header: ", header)

    rows = []
    for row in csvreader:
        print("type of row is ", type(row)) # list
        print(row)
        # for r in row:
            # print("type of r is ", type(r)) # str
            # print(r)
        rows.append(row)
    print("Total no. of rows: ", csvreader.line_num)
    print("Rows: ", rows)
    f_csv.close()
    print("Reading csv using csv module - end")

    print("\n********* read_csv_file - end")

read_csv_file()

