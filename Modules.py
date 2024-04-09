import os
import datetime
import time
# os.mkdir("week2") #creates a week2 directory
# os.mkdir("week3")
# os.mkdir("week4")
# os.rmdir("week4") #deletes the week4 directory
# os.mkdir("week2") # will not create a week2 directory because it already exists
# os.makedirs ("student/Grade/8thGrade") #creates a directory student with a subdirectory Grade and a subdirectory 8thGrade
# os.makedirs ("student/Grade/9thGrade")  #creates a directory student with a subdirectory Grade and a subdirectory 9thGrade
# os.makedirs ("student/Grade/10thGrade") #creates a directory student with a subdirectory Grade and a subdirectory 10thGrade
# os.makedirs ("student/Grade/9thGrade") # will not creates a directory student with a subdirectory Grade and a subdirectory 9thGrade  because it already exists.

#r==> read, w==> write, a==> append, x==> delete
# f=open('student.txt','r') #opens the file student.txt for reading
# print(f.read()) #reads the content of the file
f = open('student.txt', "a") #opens the file student.txt for writing
f.write("Abe") #writes the string in the file
f.write("amy") #writes the string in the file
f=open('student.txt','r') #opens the file student.txt for reading
print(f.read()) #reads the content of the file

# f=open('student.txt','w') #creates a file student.txt
# f.write("Abebe") #writes the string in the file
# f.write("kebede") #writes the string in the file