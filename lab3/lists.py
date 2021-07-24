# Create a list
L = ["Michael Jackson", 10.1, 1982]
print(L)

# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:', L[0], '\n Negative:', L[-3])
print('the same element using negative and positive indexing:\n Postive:', L[1], '\n Negative:', L[-2])
print('the same element using negative and positive indexing:\n Postive:', L[2], '\n Negative:', L[-1])

a_ = ["Michael Jackson", 10.1, 1999, [1, 2], ("A", 1)]
print(a_)
print(a_[-1][1])

# Sample List
L = ["Michael Jackson", 10.1, 1982, "MJ", 1]
print(L)
print(L[3:5])
L.extend("pop", )
L.extend(["pop", 10])
print(L)
print(L[-1])

L.append(["pop", 10])
print(L)
print(L[-1])

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

del (A[0])
print(A)

print("my name is parvin".split())
print("my name is parvin".split(','))
print("my name is parvin".split(' '))
print("my name is parvin".split('m'))

# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

A_ = [1]
A_.append([2, 3, 4, 5])
print(A_)


print("Hello Mike".split())
