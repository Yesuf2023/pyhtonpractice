
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
f=1
while f<6:
    f+=1
    if f==3:
        continue
    print(f)

'''
k=1
while k<6:
    print(k)
    k+=1
else:
    print("It is 6 or loop is finished.") # The else statement will run when the loop is finished.
'''
#For loop example