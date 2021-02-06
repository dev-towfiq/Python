print("Towfiq")
age=15
print(age)

string1="This is my string"
print(string1)

firstName="Justin"
lastName="Timberlake"

print(firstName+" "+lastName)

#User Input
#Type Casting
bdayYear=input("Input your Birthday Year:")
age=2021-int(bdayYear) #String to Interger
print("Your Age is:",age)
print("Your age is:" + str(age)) #Alternative way 

#conditional statement
price=500
if price>500:
    print("Price is Greater than 500")
elif price<0:  
    print("None")
else:
    print("Price is not grater than 500")

#List
ages=[13,15,45,96,74]

#for loop
for age in ages:
    print("Age:",age)

#for loop range
for num in range (0,10):
    print(num)

#While loop
num=0
while num<10:
        print(num)
        num=num+1

#Define Function
def brushTeeth():
    print("Brushing....")    
#Call Function
brushTeeth()