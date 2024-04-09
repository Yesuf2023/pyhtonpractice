# Example for list
    #use sqaure brackets []
    #duplicate allowed
    #ordered
    #mmutable (changeable)
    #indexed
# student = ["John","Jim" "Jennie", "Jim", "Jack", "Jim", "Joe"]
# # print(student) # The print will print all the elements of the list.
# # print (student[0:2]) # The list will print the first two elements of the list.
# # print(student[3]) # The list will print the fourth element of the list.
# # print(student[-1]) # The list will print the last element of the list.
# # print(student[-2]) # The list will print the second last element of the list.
# # print(student[1:]) # The list will print all the elements of the list except the first element.
# # print(student[:3]) # The list will print the first three elements of the list.
# # print(student[1:4]) # The list will print the second, third and fourth elements of the list.
# print(student[1:4:2]) # The list will print the second and fourth elements of the list.
# #replace the element of the list
# student[2]="James"# The list will replace the third element of the list with "James".
# print(student)

#example of tuple
    #use parentheses()
    #duplicate allowed
    #ordered
    #immutable (unchangeable)
    #indexed
# Teachers=("Mr. John", "Mr. Joe", "Mrs. Jennie", "Mr. Joe", "Mr. Jim", "Mrs. Jack", "Mr. Joe")
# print(Teachers) # The print will print all the elements of the tuple.
# print (Teachers[0:2]) # The tuple will print the first two elements of the tuple.
# print(Teachers[3]) # The tuple will print the fourth element of the tuple.
# print(Teachers[-1]) # The tuple will print the last element of the tuple.
# print(Teachers[-2]) # The tuple will print the second last element of the tuple.

#Example of Set
    #use curly brackets {}
    #noduplicate, consider only unique elements 
    #unordered
    #immutable (unchangeable)
    #unindexed
# studentSet = {"John", "Joe", "Jennie", "Jim", "Jack", "Joe", "John"}
# print(studentSet) # The print will print all the elements of the set.

#Example of Dictionary
    #use curly brackets {}
    #noduplicate, consider only unique elements 
    #unordered
    #mutable (changeable)
    #indexed
    #have key-value pair
studentDict = {"fname": "John", "lname": "Doe", "age": 25, "city": "New York"}
# print(studentDict) # The print will print all the elements of the dictionary.
# print(studentDict["age"]) # The dictionary will print the value of the key "fname".
studentDict.pop("age") # The dictionary will remove the key "age" and its value.
studentDict["gender"] = "male" # The dictionary will add a new key "gender" with the value "male".  
print(studentDict) # The print will print all the elements of the dictionary considering the updated age and gender data.


