tuple1 = ("disco", 1, 1, 2, 4.3)

print(type(tuple1))
print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

print(tuple1[-1])

tuple2 = tuple1 + ("Ayla", 3, '111')

print(tuple2)

# Slice from index 0 to index 2
print(tuple2[0:3])
print(tuple2[4:-2])

print(len(tuple1))
print(len(tuple2))

ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

ratings2 = ("Aa", "Ba", "Ab", "G", "W", "Q", "Z", "O")

ratings3 = (("Aa", "Ba"), ("Ab", "G", "W", "Q"), ("Z", "O"))

sortedRatings = sorted(ratings)
sortedRatings2 = sorted(ratings2)
sortedRatings3 = sorted(ratings3)

print(sortedRatings)
print(sortedRatings2)
print(sortedRatings3)

NestedT = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))
t_ = NestedT[2][1][1]
print(t_)

nested_t_ = NestedT[4][1][1]
print(nested_t_)

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock",
                "R&B", "progressive rock", "disco")

