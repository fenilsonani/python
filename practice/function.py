def sum(a,b):
    return a+b


fenil=sum(1,10)
print(fenil)
print(sum(1,10))

# dynamic function example

def sum(*value):
    sumf=0;
    for i in value:
        sumf+=i;
    return sumf

print(sum(1,2,3,4))