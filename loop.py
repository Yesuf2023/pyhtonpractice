
# While loop example
# The loop will run until i is less than 6, printing the value of i each time.
# The value of i is increased by 1 each time the loop runs.
# The loop will print the numbers 1 to 5.
# The loop will not print the number 6 because the condition is i<6.
# The loop will not print the number 0 because the initial value of i is 1.
'''
i=1
while i<6:
    print(i)
    i+=1

    
    # The break statement will stop the loop when j is equal to 3.
j=1
while j<6:
    print(j)
    if j==3:
        break 
    j+=1
'''

# The continue statement will skip the rest of the loop when f is equal to 3.
# f=1
# while f<6:
#     f+=1
#     if f==3:
#         continue
#     print(f)

'''
k=1
while k<6:
    print(k)
    k+=1
else:
    print("It is 6 or loop is finished.") # The else statement will run when the loop is finished.
'''
#For loop example
# student = ["John", "Jennie", "Jim", "Jack", "Joe"]
# for s in student:
#     print(s)

# name ="Yesuf Mohammed"
# for x in name:
#     print(x) #

# for n in range(6):
#     print(n) # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number, here 6 but doesn't include 6.

# for n in range[2,6]:
#     print(n) # The range() function returns a sequence of numbers, starting from 2 and ends at 6 .
# for n in range(2,6):
#     print(n) # The range() function returns a sequence of numbers, starting from 2 and ends at 6 but doesn't include 6.

# for n in range(2,16,2):
#     print(n) # The range() function returns a sequence of numbers, starting from 2 and ends at 16 but doesn't include 16. The increment value is 2.

# Nested loop example
# Nested loop is a loop inside a loop.
# The inner loop will be executed one time for each iteration of the outer loop.
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for a in adj:
#     for f in fruits:
#         print(a, f) # The inner loop will be executed one time for each iteration of the outer loop. The outer loop will run 3 times because there are 3 items in the adj list. The inner loop will run 3 times because there are 3 items in the fruits list. The inner loop will be executed 9 times in total.
# fName=["rose", "mary", "Leila", "kedja"]
# lName=["Smith", "Johnson", "Muhe", "Kedir"]
# for F in fName:
#     for L in lName:
#         print(F, L) # The inner loop will be executed one time for each iteration of the outer loop. The outer loop will run 4 times because there are 4 items in the fName list. The inner loop will run 4 times because there are 4 items in the lName list. The inner loop will be executed 16 times in total.

fName=["rose", "mary", "Leila", "kedja"]
lName=["Smith", "Johnson", "Muhe", "Kedir"]
FName= "fName"+ " " + "lName"
print(FName) #
