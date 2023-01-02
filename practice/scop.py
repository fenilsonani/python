# defined to a global scop

x=500
print(x)
def scop():
    global x
    x=300
    print(x)

scop()
print(x)

# not defined a global scop

x=500
print(x)
def scop():
    x=300
    print(x)

scop()
print(x)