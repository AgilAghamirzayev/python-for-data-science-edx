def f1(input_):
    """
    add 1 to input
    :param input_:
    :return: output
    """
    output = input_ + 1
    return output


print(f1(2))

help(f1)


def ACDC(y):
    print(rating)
    return rating + y


rating = 9

z = ACDC(1)
print(rating)
print(z)


def pink_floyd():
    global claimed_sales
    claimed_sales = "16 million"
    return claimed_sales


pink_floyd()
print(claimed_sales)


#
# You can define functions to provide the required functionality. Here are simple rules to define a function in Python:
#
# Functions blocks begin def followed by the function name and parentheses ().
# There are input parameters or arguments that should be placed within these parentheses.
# You can also define parameters inside these parentheses.
# There is a body within every function that starts with a colon (:) and is indented.
# You can also place documentation before the body.
# The statement return exits a function, optionally passing back a value.

def mul(a, b):
    c = a * b
    return c
    print("This not printed")


result = mul(4, 2)
print(result)


def isGoodRating(rating=4):
    if rating < 7:
        print("this album sucks it's rating is", rating)
    else:
        print("this album is good its rating is", rating)


print(isGoodRating(), isGoodRating(10))


artist = "Michael Jackson"

def printer1(artist):
    global internal_var1
    internal_var1= artist
    print(artist, "is an artist")


printer1(artist)
print(internal_var1)



myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

def printAll(*args):
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)


#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')


def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

print(myList)