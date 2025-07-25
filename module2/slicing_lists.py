my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing from index2 up to (but not including) index7
slice1 = my_list[2:7]
# Result: [2, 3, 4, 5, 6]

# Slicing from the beginning to a specific index
slice2 = my_list[:5]
# Result: [0, 1, 2, 3, 4]

# Slicing from a specific index to the end
slice3 = my_list[6:]
# Result: [6, 7, 8, 9]


# Slicing with a step
sliced4 = my_list[1:9:2]
# Result: [1, 3, 5, 7]

# Reversing a string using slicing
reversed_list = my_list[::-1]
# Result: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Using negative indices for slicing from the end
slice5 = my_list[-3:] # Last three elements
# Result: [7, 8, 9]

slice6 = my_list[:-4] # All elements except the last four
#Result: [0, 1, 2, 3, 4, 5]

