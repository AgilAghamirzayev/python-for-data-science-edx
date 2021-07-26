squares = ["red", "yellow", "green", "purple", "blue"]

for i, square in enumerate(squares):
    print(i + 1, square)

print(squares)
for i in range(0, 5):
    squares[i] = "white"

print(squares)

for square in squares:
    print(square)

squares.append("orange")

new_squares = []
i = 0

while squares[i] == 'white':
    new_squares.append(squares[i])
    i += 1

print(new_squares)

print(type(new_squares))

dates = [1989, 1932, 1928, 1992]
N = len(dates)
for i in range(N):
    print(dates[i])

for i in range(1, 10):
    print(i)

for year in dates:
    print(year)

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]
while year != 1973:
    print(year)
    i += 1
    year = dates[i]

print("It took ", i, "repetitions to get out of loop.")
