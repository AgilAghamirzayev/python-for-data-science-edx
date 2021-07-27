# import urllib.request
#
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# fileName = 'Example1.txt'
# urllib.request.urlretrieve(url, fileName)
#
# example1 = "Example1.txt"
# file1 = open(example1, "r")
#
# print(file1)
# print(file1.name)
# print(file1.mode)
#
# read = file1.read()
# print(read)
#
# print(type(read))
#
# file1.close()
#
# del file1
# with open(example1, "r") as file1:
#     print(file1.read(11))
#     i = 0
#     for line in file1:
#         print("Iteration", str(i), ":", line)
#         i = i + 1
#
# with open("about.txt", "r") as file2:
#     print(file2.readline())  # firstName
#     print(file2.read())  # all text
#
# # -------------------------------------------------------------------------
# # Write file
#
# # Write line to file
# exmp2 = '../resources/data/Example2.txt'
# with open(exmp2, 'w') as writefile:
#     writefile.write("This is line B\n")
#     writefile.write("This is line B\n")
#     writefile.write("This is line B\n")
#
# Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
#
# with open("../resources/data/Example3.txt", "w") as writefile:
#     for line in Lines:
#         print(line)
#         writefile.write(line)
#
# with open('Example2.txt', 'a+') as testwritefile:
#     testwritefile.write("This is line E\n")
#     print(testwritefile.read())

# with open("Example2.txt", "a+") as testwritefile:
#     print("Initial Location: {}".format(testwritefile.tell()))
#
#     data = testwritefile.read()
#     if not data:
#         print("Read nothing")
#     else:
#         print(testwritefile.read())
#
#     testwritefile.seek(0, 0)
#
#     print("New location: {}".format(testwritefile.tell()))
#     data = testwritefile.read()
#     print("New location: {}".format(testwritefile.tell()))
#     if not data:
#         print("Read nothing")
#     else:
#         print(data)
#
#     print("Location after read: {}".format(testwritefile.tell()))

# with open('Example2.txt', 'r+') as testwritefile:
#     data = testwritefile.readlines()
#     testwritefile.seek(0, 0)  # write at beginning of file
#
#     testwritefile.write("Line 1" + "\n")
#     testwritefile.write("Line 2" + "\n")
#     testwritefile.write("Line 3" + "\n")
#     testwritefile.write("finished\n")
#     # Uncomment the line below
#     # testwritefile.truncate()
#     testwritefile.seek(0, 0)
#     print(testwritefile.read())
#

with open("Example2.txt", 'r') as readfile:
    with open("Example3.xls", "w+") as writefile:
        for line in readfile:
            writefile.write(line)


for i in range(3):
    print(i)