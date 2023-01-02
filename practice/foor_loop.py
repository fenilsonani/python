fenil=["fenil",1,4,True]

for i in fenil:
    print(i)
    print(type(i))

for i in range(6):
    print(i+1)

# pattern for the print
# *
# **
# ***
# ****
# *****

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print("")

