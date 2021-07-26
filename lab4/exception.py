a = 1

try:
    b = int(input("Please enter a number to divide a "))
    a = a/b
    print("Success a = ", a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("S")
    # code to execute if there is no exception
finally:
    print("Processing Complete")
    # code to execute at the end of the try except no matter what
