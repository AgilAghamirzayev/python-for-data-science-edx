# unique
# A set is a unique collection of objects in Python. You can denote a set with a pair of curly brackets {}.
# Python will automatically remove duplicate items:

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19",
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]

album_set = set(album_list)
print(album_set)

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul",
                    "progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)

A = {"Thriller", "Black in Black", "AC/DC"}
print(A)
A.add("NSYNC")
print(A)
A.add("NSYNC")
print(A)

print("AC/DC" in A)


album_set1 = {"Thriller", 'AC/DC', 'Back in Black'}
album_set2 = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}

print(album_set1, album_set2)

intersection = album_set1 & album_set2
print(intersection)

difference = album_set1.difference(album_set2)
print(difference)

set__intersection = album_set1.intersection(album_set2)
union = album_set1.union(album_set2)

issuperset = album_set1.issuperset(album_set2)
print(issuperset)

issubset = album_set2.issubset(album_set1)
print(issubset)
