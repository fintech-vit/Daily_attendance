x = [11, 2, 41, 17, 31, 35, 42, 18, 23, 61, 43, 22, 64, 4, 14, 51, 50, 1, 37, 34, 16, 39, 65, 60, 32, 25, 13, 27, 9, 19, 8, 45, 49, 48, 20, 52, 21, 36, 38, 57, 6, 66, 68, 29, 30, 59, 3]

formatted_numbers = [f"23BFN{num:04d}" for num in x]

# Join list into a CSV string and print
for i in formatted_numbers:
    print(i)
