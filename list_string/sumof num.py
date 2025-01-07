#input list
l1 = [2,4,3,4,6,7,99,22,55,100]

#Diff methods

total_sum = sum(l1)
print("Sum of elements:", total_sum)

#                       ----------*----------
if total_sum % 2 == 0:
    print("The sum is even:",total_sum)
else:
    print("The sum is odd.")

#                       ----------*----------

num_to_check=total_sum
if num_to_check in l1:
    print("The num is available",num_to_check)
else:
    print("The",num_to_check,"number is not available" )

 #                     ----------*----------

# Print two big numbers
num1 = 0
num2 = 0
for i in l1:
      if i>num1:
             num2=num1
             num1=i
      elif i>num2 and i!=num1:
             num2=i
print(f"the first highest number is : {num1}")
print(f"the first second number is : {num2}")


l1.sort(reverse=True)
print(l1)
print(l1[0:2])