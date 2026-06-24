# traffic light
# a= str(input("enter the colors name:"))
# if(a=="red"):
#     print("stop the car")
# elif(a=="yellow"):
#     print("wait for a while")
# elif(a=="green"):
#     print("signal is clear go ahead")
# else:
#     print("invalid color name")


# b=int(input("enter the number:"))
# if(a<b):
#     print("a is less than b")
# else:
#     print("a is greate than b")

# a=int(input("enter the first number:"))
# b=int(input("enter the second number"))
# c=int(input("enter the third number:"))

# largest = a
# if b > largest:
#     largest =b
# if c > largest:
#     largest = c
# print("The largest number is :",largest)

year = int(input("Enter the year:"))
if(year % 4== 0 and year % 100  !=0 or year % 400 ==0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


