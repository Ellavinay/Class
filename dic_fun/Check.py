#Check if a Given Key Already Exists in Dictionary
dict={'first_name' : 'Jim', 'age' : 23, 'height' : 6.0 , 'job' : 'developer', 'company': 'XYZ'}
n="height"
if n in dict :
    print(f"the data {n} is present")
else:
    print(f"the data {n} is not present")