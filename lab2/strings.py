name = "Michael Jackson"
print(name)
print(name[0])
print(name[-1])
print(name[-0])
# print(name[-111])  IndexError: string index out of range
# print(name[111]) IndexError: string index out of range

# Slicing
print(name[0:4])
print(name[-1:-11])
print(name[9:13])

print(name[2::])
print(name[::2])

# Get every second element in the range from index 0 to index 4
print(name[0:5:2])

statement = name + "is the best"
print(statement)

# >Escape Sequences<
print(" Michael Jackson \n is the best")
print(" Michael Jackson \t is the best")
print(" Michael Jackson \\ is the best")
print(" Michael Jackson \r is the best")

# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Replace the old substring with the new target substring is the segment has been found in the string
a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
print(b)

print(name.find('el'))
print(name.find('Jasdfasdasdf'))

print(r"\ ")
print("\\\\")
