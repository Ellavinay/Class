# Write a  Python program to sum three given integers. However, if two values are equal, the sum will be zero.

def values(a,b,c):
    if a==b or b==c or c==a :
        return 0
    else:
       return a+b+c

print(values(10,20,30))
print(values(77,66,55))
print(values(11,22,22))
print(values(22,55,55))
print(values(55,55,55))