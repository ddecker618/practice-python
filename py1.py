#Create a list of student names
StudentList = ['John', 'Smith','Kathy','Philip']
#Call a list
print (StudentList)
#Print the first item of the list
print (StudentList[0])
#Print the second item of the list
print (StudentList[1])
#Print the third item of the list
print (StudentList[2])
#Print the third item of the list
print (StudentList[3])
#To replace Smith with Steve in the list
StudentList[1]='Steve'
#To print the updated list with Steve in place of Smith
print('The updated list is:', StudentList)
#To add a new student in the list
StudentList.append('Mark')
#To print the updated list with Mark added
print ('The updated list with a new student added is:', StudentList)
#To seach for Kathy's index in the list
IndexNumber1 = StudentList.index('Kathy')
#To print Kathy's index number in the list
print('Index for Kathy in the whole list is ', IndexNumber1)
#To delete Kathy from the list at index 2
del StudentList[2]
#To print the updated list with Kathy removed
print('The final student list after deleting Kathy is:', StudentList)
StudentList.sort()
print('The sorted list in ascending order is', StudentList)
#To sort the list in descending order
StudentList.sort(reverse=True)
print('The sorted list in descending order is:', StudentList)
StudentList.reverse()
print('The reversed list is:', StudentList)
#To slice and print the first two items on the list
print('The first two list items are', StudentList[0:2])
#To slice and print the middles items on the list
print('The middle items of the list are:', StudentList[1:3])
#To slice and print the last two items on the list
print('The last items of the list are:', StudentList[2:4])
#To modify the list items
StudentList[2:4]=['Nathan', 'Jim']
#To print the modified list
print('The list with modified items is:',StudentList)
#To use a negative index number to slice the list and print the item
print('The item with a negative index number of -1 is:',StudentList[-1])

