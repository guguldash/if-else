# Python Program to check Triangle is Valid or Not

a = int(input('Please Enter the First Angle of a Triangle: '))
b = int(input('Please Enter the Second Angle of a Triangle: '))
c = int(input('Please Enter the Third Angle of a Triangle: '))
if a+b+c==180:
     print("This is a Valid Triangle")
else:
     print( "this is an Invalid Triangle")