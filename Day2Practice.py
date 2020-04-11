"""
What we are learning today?
1. String methods
2. Control flow
3. Looping


"""

str1 = "Forsk Jaipur"
type(str1)

print (str1[0:10])

print (str1[0:100])

len(str1)


str1 = "Forsk Jaipur"

str1[0] = 'f'

#strings are read only
# strings are immutable

str1.upper() #

str1.lower()

print (str1)



str1 = "Jaipur"

str2 = str1.replace('a','A')

str1 = 'Jaipur'
str1.find('i')

dir(str)

str1 = "Shaktiman on Doordarshan"

list1 = str1.split()

print (list1)
type(list1)

str1 = "Forsk Jaipur India"

list1 = str1.split('i')


print (list1)

list1 = ["Ram", 'in', 'Jaipur']
len(list1)
str2 = " ".join(list1)
print (str2)

"".join(list1)


str1 = "delhi"
str2 = "India"

print (str1+" "+str2)

print (str1, str2)

print (str1+"2020")


#Control Flow
#if, else, elif

marks = 20

if (marks >= 33):
    print ("Pass")
    print ("Congrats")
else:
    print("Fail")
    print("Better luck next time")


marks = input("Enter the marks: ")
marks = int(marks)
#version 02
if (marks >= 60):
    print ("First Division")
elif (marks < 60 and marks >= 45):
    print("Second Divison")
elif (marks < 45 and marks >= 33):
    print ("Third Division")
else:
    print("Fail")    


#Loops
#while , for

number  = 0

while (number < 10):
    print (number)
    number = number + 1



list1 = ['Ram', 'Sita','Razia']

for item in list1:
    print (item)

for x in list1:
    print (x)

number  = 0

number++

number = number + 1

number += 1


str1 =  "Amrita College"
str1.split()






list1 = ["Pragya", 'from', 'Jaipur']


"$".join(list1)

"""
Ramzan
Ali
"""

str1 = "Jaipur India"

if len(str1) > 10:
    print ("long string")
else:
    print ("short string")


marks = 30

marks == 30

str1 = "aabca"
str1.replace('aa','$')




